"""Assemble the seed library into the documents the app stores.

Inputs:  app/seed/courses.json and app/seed/books/<course-id>/ch<N>.json (+ figure SVGs)
Outputs: app/seed/dist/<db path with / replaced by __>.json, one file per document:
  courses/<id>                 book (syllabus, bible, preface, cover, written chapters)
  courses/<id>/chapters/ch<n>  a written chapter (lesson, figures, interactives, assess, review, prov)
"""
import json
import pathlib

SEED = pathlib.Path(__file__).resolve().parent.parent / "app" / "seed"
DIST = SEED / "dist"
DIST.mkdir(exist_ok=True)
for old in DIST.glob("*.json"):
    old.unlink()

AGENT_NOTE = ("Researched and written in Claude Code by Claude research agents (configured model claude-opus-5-5), "
              "with every fact and citation checked by web search, then independently fact-checked, October 2026.")


def write(path, doc):
    out = DIST / (path.replace("/", "__") + ".json")
    out.write_text(json.dumps(doc, ensure_ascii=False, separators=(",", ":")))
    print(f"{path:55s} {out.stat().st_size:>8,d} bytes")


courses = json.loads((SEED / "courses.json").read_text())
for c in courses:
    folder = SEED / "books" / c["id"]
    written = dict(c.get("written") or {})
    for f in sorted(folder.glob("ch*.json"), key=lambda p: int(p.stem[2:])) if folder.exists() else []:
        ch = json.loads(f.read_text())
        n = ch["n"]
        figures = [{"section": x["section"], "caption": x["caption"], "svg": (folder / x["file"]).read_text().strip()}
                   for x in ch.get("figureFiles", [])]
        doc = {"n": n, "lesson": ch["lesson"], "figures": figures, "interactives": ch.get("interactives", []),
               "assess": ch["assess"], "prov": ch.get("prov") or {"note": AGENT_NOTE}, "updatedAt": 1791600000000}
        if ch.get("review"):
            doc["review"] = ch["review"]
        write(f"courses/{c['id']}/chapters/ch{n}", doc)
        written.setdefault(str(n), 1791600000000)
    c["written"] = written
    write(f"courses/{c['id']}", c)
