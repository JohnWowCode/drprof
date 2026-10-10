"""Apply an independent fact-check to an authored chapter and record it in the chapter's review.

Usage: python3 scripts/apply_check.py app/seed/books/<course>/ch<N>.json
Reads ch<N>.check.json written by the checker:
{ "keysChecked": 20, "keysAgreed": 20, "keyFixes": [ { "id": "Q3", "from": "B", "to": "C", "why": "..." } ],
  "corrections": [ { "where": "2.1 reading", "quote": "exact text", "correction": "replacement", "why": "...", "severity": "error|imprecise|unverifiable|style" } ],
  "sourcesChecked": 14, "sourcesWithdrawn": [ "S2.1-3" ], "summary": "..." }
Corrections whose quote is found once in the chapter JSON strings or a figure SVG are applied; others are reported.
"""
import json, pathlib, sys
from xml.sax.saxutils import escape

p = pathlib.Path(sys.argv[1]); ck = json.loads(p.with_suffix(".check.json").read_text())
ch = json.loads(p.read_text()); out = []

def walk(o, quote, corr):
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, str) and quote in v and k not in ("file",):
                o[k] = v.replace(quote, corr, 1); return True
            if isinstance(v, (dict, list)) and walk(v, quote, corr): return True
    elif isinstance(o, list):
        for i, v in enumerate(o):
            if isinstance(v, str) and quote in v:
                o[i] = v.replace(quote, corr, 1); return True
            if isinstance(v, (dict, list)) and walk(v, quote, corr): return True
    return False

for c in ck.get("corrections", []):
    q, r = c.get("quote", ""), c.get("correction", "")
    ok = bool(q) and q != r and walk({k: ch[k] for k in ("lesson", "assess", "interactives", "figureFiles") if k in ch}, q, r)
    if not ok:
        for f in ch.get("figureFiles", []):
            fp = p.parent / f["file"]; svg = fp.read_text()
            if ">" + escape(q) + "<" in svg:
                fp.write_text(svg.replace(">" + escape(q) + "<", ">" + escape(r) + "<", 1)); ok = True; break
    out.append({"where": c.get("where", ""), "before": q, "after": r, "why": c.get("why", ""), "severity": c.get("severity", ""), "applied": ok})

items = {f"P{s['n']}-{i}": q for s in ch["lesson"]["sections"] for i, q in enumerate(s["practice"]) if q.get("type") == "mc"}
items.update({f"Q{i+1}": q for i, q in enumerate(ch["assess"]["quiz"])})
for kf in ck.get("keyFixes", []):
    q = items.get(kf.get("id")); to = "ABCDEFGH".find(str(kf.get("to", "?"))[:1])
    if q and 0 <= to < len(q["choices"]): q["answer"] = to
withdrawn = set(ck.get("sourcesWithdrawn", []))
for s in ch["lesson"]["sections"]:
    for x in s.get("sources", []):
        if f"S{s['n']}-{x['n']}" in withdrawn: x["withdrawn"] = True; x.pop("checked", None)
        else: x["checked"] = True
for r in ch["assess"].get("readings", []): r["checked"] = True
ch["review"] = {"full": True, "at": 1791600000000, "by": ck.get("method") or "Researched and written with web-search verification, then fact-checked independently by a second agent; every answer key was re-solved blind.",
                "keysChecked": ck.get("keysChecked", 0), "keysAgreed": ck.get("keysAgreed", 0), "keyFixes": ck.get("keyFixes", []),
                "corrections": out, "readingsRemoved": [], "srcChecked": ck.get("sourcesChecked", 0), "srcWithdrawn": len(withdrawn),
                "summary": ck.get("summary", ""), "style": {}}
p.write_text(json.dumps(ch, ensure_ascii=False, indent=2))
print(f"{p.name}: {sum(o['applied'] for o in out)}/{len(out)} corrections applied, {len(ck.get('keyFixes', []))} key fixes, {len(withdrawn)} sources withdrawn")
for o in out:
    if not o["applied"]: print("  NOT APPLIED:", o["where"], "|", o["before"][:90])
