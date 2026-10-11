#!/usr/bin/env python3
"""Inspect Unity scene/prefab names. No copyrighted assets are exported."""
import collections
import re
import sys
from pathlib import Path

source=Path(sys.argv[1])
out=Path(sys.argv[2])
lines=["# Unity scene/input UI inspection", ""]
def add(s=""): lines.append(str(s))
words=("touch","mobile","control","button","btn","joy","input","canvas","gamepad","ui","dpad","attack","dash","jump","parry","spell","heal","inventory","map","hud","overlay","edit","setting")
try:
    import UnityPy
    add(f"- UnityPy: {UnityPy.__version__ if hasattr(UnityPy, '__version__') else 'installed'}")
    env=UnityPy.load(str(source))
    counts=collections.Counter()
    objects=[]
    ui_gameobjects=[]
    touch_component_refs=[]
    target_touch_gameobjects=[]
    for i,obj in enumerate(env.objects):
        name=obj.type.name
        counts[name]+=1
        if name == "MonoBehaviour":
            try:
                dat=obj.read()
                script=getattr(dat,"m_Script",None)
                path=getattr(script,"path_id",None)
                if path==399:
                    touch_component_refs.append((obj,dat))
            except Exception:
                pass
        if name in ("GameObject","MonoBehaviour","TextAsset","MonoScript","Texture2D","Sprite"):
            try:
                data=obj.read()
                objname=getattr(data,"m_Name","")
                if not objname and name=="MonoScript":
                    objname=getattr(data,"m_ClassName","")
                if name=="GameObject" and str(objname)=="MoonscarsTouchControls":
                    target_touch_gameobjects.append((obj,data))
                if name=="GameObject" and objname and any(w in str(objname).lower() for w in ("btn","touch","control","joystick","virtual","gamepad","button","dpad","spell","parry","dash","jump","attack","mobile","edit")):
                    ui_gameobjects.append(f"{str(objname)[:110]} | path ID {obj.path_id}")
                if objname and any(w in str(objname).lower() for w in words):
                    objects.append(f"{name} | {str(objname)[:160]} | path ID {obj.path_id}")
            except Exception:
                pass
    add(f"- Total Unity objects: {sum(counts.values())}")
    add("")
    add("## Type counts")
    for k,v in counts.most_common(40): add(f"- {k}: {v}")
    add("")
    add("## Objects likely part of touch/control UI")
    for s in objects[:400]: add(f"- {s}")
    if not objects: add("- No matching named objects found by UnityPy.")
    add("")
    add("## GameObjects most likely to be editable mobile buttons")
    add(f"- Matching GameObjects: {len(ui_gameobjects)}")
    for o in ui_gameobjects[:400]: add(f"- {o}")
    add("")
    add("## MoonscarsTouchControls instances")
    add(f"- MonoBehaviour script 399 matches: {len(touch_component_refs)}")
    for obj,dat in touch_component_refs[:15]:
        add(f"- MonoBehaviour object path ID {obj.path_id}; GameObject {getattr(getattr(dat,'m_GameObject',None),'path_id',None)}")
        try:
            tr=obj.read_typetree()
            add(f"- Serialized field names: {list(tr.keys())[:90]}")
        except Exception as e:
            add(f"- Type tree unavailable: {str(e)[:170]}")
except Exception as e:
    add(f"Inspection exception: {type(e).__name__}: {e}")
try:
    add("")
    add("## Attached components on MoonscarsTouchControls GameObject")
    add(f"- Matching target GameObjects: {len(target_touch_gameobjects)}")
    for target,data in target_touch_gameobjects[:10]:
        add(f"- Target object path ID: {target.path_id}")
        for comp in getattr(data,"m_Component",[])[:40]:
            try:
                ptr=getattr(comp,"component",None)
                if ptr is None and isinstance(comp,dict):
                    ptr=comp.get("component")
                if ptr is None: ptr=getattr(comp,"m_Component",None)
                item=ptr.get_obj() if hasattr(ptr,"get_obj") else None
                if item is None:
                    add(f"  - Missing component; raw reference: {str(comp)[:150]}")
                    continue
                add(f"  - {item.type.name}, object path ID {item.path_id}")
                if item.type.name=="MonoBehaviour":
                    d=item.read()
                    scr=getattr(d,"m_Script",None)
                    scr_name="unknown"
                    try:
                        scr_obj=scr.get_obj()
                        if scr_obj:
                            scr_name=str(getattr(scr_obj.read(),"m_ClassName","unknown"))
                    except Exception: pass
                    add(f"    - Script: {scr_name}")
                    try:
                        tr=item.read_typetree()
                        add(f"    - Serialized fields: {list(tr.keys())[:100]}")
                        for k,v in list(tr.items())[:100]:
                            if isinstance(v,(str,int,float,bool)) and len(str(v))<=120:
                                add(f"    - {k} = {v}")
                            elif isinstance(v,list):
                                add(f"    - {k}: array ({len(v)} items)")
                    except Exception as e: add(f"    - Serialized data unavailable: {str(e)[:130]}")
            except Exception as e:
                add(f"  - Could not inspect component: {str(e)[:130]}")
except Exception as e:
    add(f"Touch hierarchy scan error: {e}")

out.write_text("\n".join(lines)+"\n",encoding="utf-8")
print("\n".join(lines)[:18000])
