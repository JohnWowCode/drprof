"""Turn an authored chapter into narration tracks: one track for the opening, one per section.

The words stay the textbook's own; only what cannot be heard changes (citation markers,
markdown, a few symbols). Writes ch<N>.narration.json beside the chapter.
Usage: python3 scripts/narration_script.py app/seed/books/<course>/ch<N>.json [...]
"""
import json, re, sys
from pathlib import Path

COURSES = {c["id"]: c for c in json.load(open(Path(__file__).parent.parent / "app/seed/courses.json"))}

def speakable(t):
    t = re.sub(r"\s*\[\d+(?:\s*[,–-]\s*\d+)*\]", "", t)          # citation markers [1], [2, 3]
    t = re.sub(r"\*\*|\*|`", "", t)                               # markdown
    t = t.replace("≈", "about ").replace("~", "about ").replace("×", " times ").replace("−", "minus ")
    t = re.sub(r"(\d)\s*°C\b", r"\1 degrees Celsius", t)
    t = re.sub(r"(\d)\s*°", r"\1 degrees", t)
    t = re.sub(r"(\d)\s*%", r"\1 percent", t)
    t = re.sub(r"\bkm/h\b", "kilometres per hour", t)
    t = re.sub(r"\bm/s\b", "metres per second", t)
    t = re.sub(r"\s{2,}", " ", t)
    return t.strip()

def tracks(path):
    ch = json.load(open(path)); n = ch["n"]; L = ch["lesson"]
    course = COURSES[path.parent.name]
    title = course["chapters"][n - 1]["title"]
    out = [{"label": "Opening", "text": " ".join([f"Chapter {n}. {title}.", speakable(L.get("hook", "")), speakable(L.get("overview", ""))]).strip()}]
    for s in L["sections"]:
        paras = [f"Section {s['n'].replace('.', ' point ')}. {s['title']}."] + [speakable(p) for p in s["reading"]]
        m = s.get("misconception") or {}
        if m.get("myth"):
            paras.append(f"A common misconception: {speakable(m['myth'])} In fact, {speakable(m['fact'])}")
        out.append({"label": f"{s['n']} {s['title']}", "text": " ".join(paras)})
    return out

if __name__ == "__main__":
    for a in sys.argv[1:]:
        p = Path(a); t = tracks(p)
        dest = p.with_name(p.stem + ".narration.json")
        json.dump({"tracks": t}, open(dest, "w"), ensure_ascii=False, indent=1)
        print(f"{dest.parent.name}/{dest.name}: {len(t)} tracks, {sum(len(x['text']) for x in t):,} characters, longest {max(len(x['text']) for x in t):,}")
