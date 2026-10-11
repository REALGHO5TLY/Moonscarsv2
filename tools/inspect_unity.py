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
out.write_text("\n".join(lines)+"\n",encoding="utf-8")
print("\n".join(lines)[:18000])
