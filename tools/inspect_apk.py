#!/usr/bin/env python3
"""Metadata-only APK inspector: never commits or redistributes game assets."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import subprocess
import sys
import zipfile

apk = Path(sys.argv[1])
out = Path(sys.argv[2])
out.parent.mkdir(parents=True, exist_ok=True)
lines = ["# Moonscars Android APK: technical inspection", ""]
def add(s=""):
    lines.append(str(s))
def code(cmd):
    try:
        p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=45)
        return p.stdout[:15000] or "(no output)"
    except Exception as e:
        return f"Unavailable: {e}"
add(f"- Filename: `{apk.name}`")
add(f"- File size: {apk.stat().st_size:,} bytes")
add(f"- SHA-256: `{sha256(apk.read_bytes()).hexdigest()}`")
try:
    with zipfile.ZipFile(apk) as z:
        if z.testzip() is not None:
            raise ValueError("CRC failed: file is corrupt")
        names = z.namelist()
        files = [i for i in z.infolist() if not i.is_dir()]
        add(f"- ZIP entries: {len(files)}")
        add(f"- DEX files: {', '.join(n for n in names if n.endswith('.dex')) or 'none'}")
        add("")
        add("## Likely port engine")
        indicators = {
            "Unity": ["assets/bin/Data/", "libunity.so", "libil2cpp.so"],
            "Godot": ["libgodot_android.so", ".pck", "libgodot.so"],
            "GameMaker": ["libyoyo.so", "assets/game.droid", "data.win"],
            "SDL / native": ["libSDL2.so", "libSDL3.so"],
            "Ren'Py": ["renpy/", "librenpy.so"],
            "WebView / HTML": ["assets/www/", "index.html", "cordova.js"],
            "MonoGame / FNA": ["libmonosgen", "Content/"],
            "Switch emulator": ["libskyline.so", "libeden.so", "libyuzu.so"],
        }
        lower = [n.lower() for n in names]
        for label, patterns in indicators.items():
            matches = [pattern for pattern in patterns if any(pattern.lower() in path for path in lower)]
            if matches:
                add(f"- **{label}** indicators: {', '.join(matches)}")
        add("")
        add("## Native libraries")
        libs=[i for i in files if i.filename.startswith("lib/") and i.filename.endswith(".so")]
        for i in sorted(libs,key=lambda i:i.filename)[:150]:
            add(f"- `{i.filename}` ({i.file_size:,} bytes)")
        if not libs: add("- none")
        add("")
        add("## Top-level and assets overview")
        categories=Counter(n.split("/")[0] for n in names)
        for a,b in categories.most_common(35): add(f"- {a}: {b} entries")
        add("")
        add("## Potential control mappings/config resources")
        keywords=("touch","input","control","button","joystick","keymap","keyboard","gamepad","controller","overlay","config","prefs")
        for i in files:
            if any(w in i.filename.lower() for w in keywords) and i.file_size < 2000000:
                add(f"- `{i.filename}` ({i.file_size:,} bytes)")
                if len(lines)>650: break
        add("")
        add("## APKVision control configuration structure")
        import json
        if "assets/AVConfig.json" in names:
            try:
                obj = json.loads(z.read("assets/AVConfig.json").decode("utf-8-sig"))
                def short(v):
                    if isinstance(v, dict):
                        return f"object with {len(v)} keys"
                    if isinstance(v, list):
                        return f"array of {len(v)} items"
                    s=str(v).replace("\\n"," ")
                    return (s[:96]+"…" if len(s)>96 else s)
                add(f"- Root type: {type(obj).__name__}")
                if isinstance(obj,dict):
                    for k,v in list(obj.items())[:100]:
                        add(f"- Root \`{k}\`: {short(v)}")
                elif isinstance(obj,list):
                    add(f"- Root items: {len(obj)}")
                add("")
                add("### Matching input / touch / menu paths")
                match_words=("touch","input","control","button","joystick","keymap","keyboard","gamepad","controller","overlay","bind","press","stick","dpad","opacity","scale","position","size","toggle","axis","hud","gesture","keycode")
                hits=[]
                def visit(node,path,depth=0):
                    if depth>11 or len(hits)>=230: return
                    if isinstance(node,dict):
                        for k,v in node.items():
                            kp=f"{path}.{k}"
                            if any(w in kp.lower() for w in match_words):
                                hits.append((kp,short(v)))
                            visit(v,kp,depth+1)
                    elif isinstance(node,list):
                        for i,v in enumerate(node[:45]):
                            visit(v,f"{path}[{i}]",depth+1)
                visit(obj,"root")
                if hits:
                    for p,v in hits:
                        add(f"- \`{p}\`: {v}")
                else:
                    add("- No matching labels; the configuration may use numeric or obfuscated field names.")
            except Exception as e:
                add(f"- Unable to parse AVConfig.json as JSON: {e}")
        add("")
        add("## Full entry and size inventory")
        for i in sorted(files,key=lambda v:v.filename):
            add(f"- {i.filename}: {i.file_size:,} B")
        add("")
        add("## APKVision configuration binary identification")
        if "assets/AVConfig.json" in names:
            b = z.read("assets/AVConfig.json")
            add(f"- First 64 bytes (hex): {b[:64].hex()}")
            add(f"- Printable prefix: {repr(b[:80])}")
            add(f"- ZIP magic: {b.startswith(bytes.fromhex('504b0304'))}")
            add(f"- GZIP magic: {b.startswith(bytes.fromhex('1f8b'))}")
        add("")
        add("## Input-related readable strings (for locating existing overlay)")
        import re
        for file_to_check in ["classes.dex","lib/arm64-v8a/libAPKVISION.so","lib/arm64-v8a/libil2cpp.so"]:
            if file_to_check not in names:
                continue
            raw=z.read(file_to_check)
            matches=[]
            for m in re.finditer(rb"[ -~]{6,150}",raw):
                s=m.group(0).decode("ascii","ignore").strip()
                if any(k in s.lower() for k in ("joystick","touchcontrol","touchscreen","keycode","virtualbutton","gamepad","buttonmapping","inputbridge","dpad","unitysendmessage","controllerlayout","controllerconfig","avconfig","keyevent","moonscars")):
                    if s not in matches and len(s)<150:
                        matches.append(s)
                if len(matches)>=75: break
            add(f"### {file_to_check}")
            for s in matches: add(f"- \`{s.replace(chr(96),'')}\`")
            if not matches: add("- No clear-text matches")
        add("")

        add("## Android classes present in the port")
        dex=z.read("classes.dex")
        classnames=sorted(set(m.group(0).decode("ascii","ignore") for m in __import__("re").finditer(rb"L(?:com|org|androidx)/[A-Za-z0-9_/$]{4,};", dex)))
        for name in classnames[:240]:
            add(f"- \`{name}\`")
        add("")

        add("## Unity IL2CPP control and interface type names")
        meta_name="assets/bin/Data/Managed/Metadata/global-metadata.dat"
        if meta_name in names:
            import re
            data=z.read(meta_name)
            strs=[]
            for mm in re.finditer(rb"[A-Za-z_][A-Za-z0-9_:.+ /-]{4,105}",data):
                s=mm.group(0).decode("ascii","ignore").strip()
                if any(w in s.lower() for w in ("touch", "control", "joystick", "input", "gamepad", "canvas", "virtual", "keyboard", "button", "overlay", "keybind", "keycode", "ui", "attack", "parry", "heal", "witchery")) and s not in strs:
                    strs.append(s)
                if len(strs)>=220: break
            for s in strs: add(f"- \`{s.replace(chr(96),'')}\`")
        add("")
        add("## Android manifest / package information")
        add("~~~")
        command = ["aapt","dump","badging",str(apk)]
        add(code(command))
        add("~~~")
except Exception as e:
    add(f"ERROR reading APK: {type(e).__name__}: {e}")
out.write_text("\n".join(lines)+"\n")
print("\n".join(lines)[:24000])
