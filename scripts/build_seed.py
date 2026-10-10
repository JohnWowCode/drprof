"""Assemble the seed library (app/seed/*.json + *.svg) into the documents the app stores.

Writes app/seed/dist/<db path with / replaced by __>.json, one file per document:
  courses/<id>                 course syllabus
  courses/<id>/chapters/ch<n>  a written chapter (lesson, figures, assess)
"""
import json
import pathlib

SEED = pathlib.Path(__file__).resolve().parent.parent / "app" / "seed"
DIST = SEED / "dist"
DIST.mkdir(exist_ok=True)


def write(path, doc):
    out = DIST / (path.replace("/", "__") + ".json")
    out.write_text(json.dumps(doc, ensure_ascii=False, separators=(",", ":")))
    print(f"{path:55s} {out.stat().st_size:>7,d} bytes")


courses = json.loads((SEED / "courses.json").read_text())
for c in courses:
    write(f"courses/{c['id']}", c)

ch = json.loads((SEED / "birds-ch1.json").read_text())
figures = [
    {"section": f["section"], "caption": f["caption"], "svg": (SEED / f["file"]).read_text().strip()}
    for f in ch.pop("figureFiles")
]
doc = {"n": ch["n"], "lesson": ch["lesson"], "figures": figures, "assess": ch["assess"], "review": ch["review"], "prov": ch["prov"], "updatedAt": 1760004000000}
write("courses/birds-beginner-seed/chapters/ch1", doc)
