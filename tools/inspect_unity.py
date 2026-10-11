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
    for i,obj in enumerate(env.objects):
        name=obj.type.name
        counts[name]+=1
        if name in ("GameObject","MonoBehaviour","TextAsset","MonoScript","Texture2D","Sprite"):
            try:
                data=obj.read()
                objname=getattr(data,"m_Name","")
                if not objname and name=="MonoScript":
                    objname=getattr(data,"m_ClassName","")
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
except Exception as e:
    add(f"Inspection exception: {type(e).__name__}: {e}")
out.write_text("\n".join(lines)+"\n",encoding="utf-8")
print("\n".join(lines)[:18000])
