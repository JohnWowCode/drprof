"""Check course plans in app/seed/plans/*.json and merge them into app/seed/courses.json (replace by id)."""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
LEN = {"short": 5, "standard": 8, "full": 12}
LEVELS = {"noob", "beginner", "intermediate", "advanced", "expert", "mastery"}

def problems(c):
    P = []
    for k in ("id", "topic", "level", "length", "code", "title", "department", "description", "chapters", "color", "preface", "coverSvg", "bible"):
        if not c.get(k): P.append(f"missing {k}")
    if c.get("level") not in LEVELS: P.append(f"bad level {c.get('level')!r}")
    want = LEN.get(c.get("length"))
    if want and len(c.get("chapters", [])) != want: P.append(f"{len(c['chapters'])} chapters, want {want}")
    for i, ch in enumerate(c.get("chapters", []), 1):
        if not 3 <= len(ch.get("sections", [])) <= 4: P.append(f"chapter {i}: {len(ch.get('sections', []))} sections")
        if not ch.get("challenge"): P.append(f"chapter {i}: no challenge")
    if not re.fullmatch(r"#[0-9A-Fa-f]{6}", c.get("color", "")): P.append("bad color")
    if not str(c.get("coverSvg", "")).startswith("<svg"): P.append("cover is not svg")
    if "<text" in str(c.get("coverSvg", "")): P.append("cover contains text")
    b = c.get("bible", {})
    if not 4 <= len(b.get("canon", [])) <= 10: P.append(f"canon has {len(b.get('canon', []))} entries")
    blob = json.dumps(c, ensure_ascii=False)
    if "—" in c.get("preface", "") + c.get("description", ""): P.append("em dash in preface/description")
    return P

courses = json.load(open(ROOT / "app/seed/courses.json"))
ids = [c["id"] for c in courses]
bad = 0
for f in sorted((ROOT / "app/seed/plans").glob("*.json")):
    c = json.load(open(f))
    c.setdefault("written", {}); c.setdefault("persona", "professor"); c.setdefault("engine", "default"); c.setdefault("v", 1)
    P = problems(c)
    print(f"{f.name}: {'OK' if not P else '; '.join(P)}  ({c.get('code')} {c.get('title')!r}, {len(c.get('chapters', []))} ch)")
    if P: bad += 1; continue
    if c["id"] in ids: courses[ids.index(c["id"])] = c
    else: courses.append(c); ids.append(c["id"])
if "--write" in sys.argv:
    json.dump(courses, open(ROOT / "app/seed/courses.json", "w"), ensure_ascii=False, indent=1)
    print(f"wrote courses.json: {len(courses)} courses")
sys.exit(1 if bad else 0)
