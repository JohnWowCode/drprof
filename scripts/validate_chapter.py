"""Validate a hand-authored chapter file for the Dr. Professor seed library.

Usage: python3 scripts/validate_chapter.py app/seed/books/<course-id>/ch<N>.json
Prints PROBLEMS (must fix) and NOTES, exits 1 if there are problems.
"""
import json, pathlib, re, sys, xml.dom.minidom

BANNED = ["delve", "tapestry", "testament to", "in the realm of", "embark", "unlock", "unleash", "harness", "foster", "crucial",
          "pivotal", "vibrant", "intricate", "myriad", "multifaceted", "seamless", "paramount", "underscore", "showcase",
          "leverage", "game-changer", "ever-evolving", "it's important to note", "it is important to note", "it is worth noting",
          "in conclusion", "in summary", "at its core", "let's dive in", "fascinating world", "navigate the", "journey of", "landscape of"]
FUNCS = {"sqrt", "abs", "sin", "cos", "tan", "log", "log10", "exp", "min", "max", "pow", "round", "floor", "ceil"}
TYPES = {"explorer", "sort", "order", "timeline", "scale", "case", "sim"}

def check_expr(expr, names):
    toks = re.findall(r"\s*(\d+\.?\d*(?:[eE][-+]?\d+)?|[A-Za-z_][A-Za-z_0-9]*|\*\*|[-+*/^(),])", expr)
    if "".join(t.strip() for t in toks) != re.sub(r"\s+", "", expr):
        return f"unsupported characters in expression: {expr!r}"
    for i, t in enumerate(toks):
        t = t.strip()
        if re.match(r"[A-Za-z_]", t):
            nxt = toks[i + 1].strip() if i + 1 < len(toks) else ""
            if nxt == "(":
                if t not in FUNCS: return f"unknown function {t!r} in {expr!r}"
            elif t not in names and t not in ("pi", "e"):
                return f"unknown name {t!r} in {expr!r}"
    depth = 0
    for t in toks:
        depth += t.strip() == "("; depth -= t.strip() == ")"
        if depth < 0: return f"unbalanced parentheses in {expr!r}"
    return None if depth == 0 else f"unbalanced parentheses in {expr!r}"

def main(path):
    p = pathlib.Path(path); P, N = [], []
    try: ch = json.loads(p.read_text())
    except Exception as e: print("PROBLEMS\n- invalid JSON:", e); return 1
    course = p.parent.name
    syl = {c["id"]: c for c in json.loads((pathlib.Path(__file__).resolve().parent.parent / "app/seed/courses.json").read_text())}.get(course)
    n = ch.get("n")
    if not syl: P.append(f"unknown course folder {course}")
    else:
        sylch = syl["chapters"][n - 1]
        want = [f"{n}.{j+1}" for j in range(len(sylch["sections"]))]
    L = ch.get("lesson") or {}; A = ch.get("assess") or {}
    for k in ("hook", "overview"):
        if len(str(L.get(k, ""))) < 80: P.append(f"lesson.{k} missing or too short")
    secs = L.get("sections", [])
    if syl and [s.get("n") for s in secs] != want: P.append(f"section numbers {[s.get('n') for s in secs]} != syllabus {want}")
    text = []
    for s in secs:
        sn = s.get("n"); rd = s.get("reading", [])
        if not 4 <= len(rd) <= 7: P.append(f"{sn}: {len(rd)} reading paragraphs (want 4-7)")
        srcn = {x.get("n") for x in s.get("sources", [])}
        if len(srcn) < 2: P.append(f"{sn}: fewer than 2 sources")
        for x in s.get("sources", []):
            if not x.get("citation") or not x.get("supports"): P.append(f"{sn}: source {x.get('n')} missing citation or supports")
        used = set()
        for para in rd:
            text.append(para)
            for m in re.finditer(r"\[(\d+(?:\s*[,–-]\s*\d+)*)\]", para):
                for num in re.findall(r"\d+", m.group(1)): used.add(int(num))
        if used - srcn: P.append(f"{sn}: citation numbers {sorted(used - srcn)} have no source")
        if srcn - used: N.append(f"{sn}: sources {sorted(srcn - used)} never cited in the text")
        if not 3 <= len(s.get("keyTerms", [])) <= 7: P.append(f"{sn}: {len(s.get('keyTerms', []))} key terms (want 3-6)")
        ex = s.get("example") or {}
        if len(ex.get("steps", [])) < 3: P.append(f"{sn}: worked example needs 3+ steps")
        mc = s.get("misconception") or {}
        if not mc.get("myth") or not mc.get("fact"): P.append(f"{sn}: misconception missing")
        pr = s.get("practice", [])
        if len(pr) != 3: P.append(f"{sn}: {len(pr)} practice problems (want 3)")
        for i, q in enumerate(pr):
            if q.get("type") == "mc":
                if not (isinstance(q.get("answer"), int) and 0 <= q["answer"] < len(q.get("choices", []))): P.append(f"{sn} practice {i}: bad answer index")
            elif q.get("type") != "short": P.append(f"{sn} practice {i}: type must be mc or short")
            text.append(q.get("explanation", ""))
        text += ex.get("steps", []) + [mc.get("myth", ""), mc.get("fact", "")]
    quiz = A.get("quiz", [])
    if len(quiz) != 8: P.append(f"quiz has {len(quiz)} questions (want 8)")
    for i, q in enumerate(quiz):
        if not (isinstance(q.get("answer"), int) and 0 <= q["answer"] < len(q.get("choices", []))): P.append(f"quiz {i+1}: bad answer index")
        if syl and q.get("sec") not in want: P.append(f"quiz {i+1}: sec {q.get('sec')!r} not a section of this chapter")
    pos = [q.get("answer") for q in quiz]
    if quiz and max(pos.count(k) for k in set(pos)) > 4: N.append(f"quiz answer positions are unbalanced: {pos}")
    if not 8 <= len(A.get("slides", [])) <= 12: P.append(f"{len(A.get('slides', []))} slides (want 8-12)")
    if len(A.get("challenge", [])) != 2: P.append("need exactly 2 challenge exercises")
    if not 3 <= len(A.get("readings", [])) <= 5: P.append("need 3-5 readings")
    for f in ch.get("figureFiles", []):
        fp = p.parent / f.get("file", "")
        if not fp.exists(): P.append(f"figure file missing: {fp.name}"); continue
        try: xml.dom.minidom.parseString(fp.read_text())
        except Exception as e: P.append(f"{fp.name}: invalid SVG/XML: {e}")
        if 'viewBox="0 0 800 480"' not in fp.read_text(): P.append(f"{fp.name}: viewBox must be 0 0 800 480")
        if not f.get("caption"): P.append(f"{fp.name}: caption missing")
    if not 2 <= len(ch.get("figureFiles", [])) <= 4: P.append("need 2-4 figures")
    its = ch.get("interactives", [])
    core = [x for x in its if x.get("type") != "sim"]
    if not 2 <= len(core) <= 4: P.append(f"{len(core)} interactives besides follow-alongs (want 2-4)")
    for i, it in enumerate(its):
        t = it.get("type"); tag = f"interactive {i+1} ({t})"
        if t not in TYPES: P.append(f"{tag}: unknown type"); continue
        if syl and it.get("section") not in want: P.append(f"{tag}: section {it.get('section')!r} not in chapter")
        if not it.get("title"): P.append(f"{tag}: title missing")
        if t == "explorer":
            names = {x.get("id") for x in it.get("inputs", [])} | set((it.get("constants") or {}).keys())
            for x in it.get("inputs", []):
                if not all(k in x for k in ("id", "label", "min", "max", "step", "value")): P.append(f"{tag}: input missing fields")
                elif not x["min"] <= x["value"] <= x["max"]: P.append(f"{tag}: input {x['id']} value outside min/max")
            if not it.get("outputs"): P.append(f"{tag}: no outputs")
            for o in it.get("outputs", []):
                err = check_expr(str(o.get("expr", "")), names)
                if err: P.append(f"{tag}: {err}")
        if t == "sort":
            nb = len(it.get("buckets", []))
            if nb < 2 or len(it.get("items", [])) < 4: P.append(f"{tag}: need 2+ buckets and 4+ items")
            for x in it.get("items", []):
                if not (isinstance(x.get("bucket"), int) and 0 <= x["bucket"] < nb) or not x.get("why"): P.append(f"{tag}: item {x.get('text')!r} bad bucket or missing why")
        if t == "order" and len(it.get("steps", [])) < 4: P.append(f"{tag}: need 4+ steps")
        if t == "timeline" and (len(it.get("events", [])) < 4 or any("t" not in x or not x.get("label") for x in it.get("events", []))): P.append(f"{tag}: need 4+ events with t and label")
        if t == "scale" and (len(it.get("items", [])) < 3 or any(not isinstance(x.get("value"), (int, float)) or x["value"] <= 0 for x in it.get("items", []))): P.append(f"{tag}: need 3+ items with positive numeric values")
        if t == "case" and len(it.get("steps", [])) < 2: P.append(f"{tag}: need 2+ steps")
        if t == "sim":
            if len(it.get("steps", [])) < 3 or any(not x.get("do") for x in it.get("steps", [])): P.append(f"{tag}: need 3+ steps, each with 'do'")
            ck = it.get("check")
            if ck and not (ck.get("q") and len(ck.get("choices", [])) >= 2 and isinstance(ck.get("answer"), int) and 0 <= ck["answer"] < len(ck["choices"])): P.append(f"{tag}: bad check question")
    blob = " ".join(text + [L.get("hook", ""), L.get("overview", "")]).lower()
    for w in BANNED:
        if w in blob: P.append(f"banned phrase: {w!r}")
    if "—" in blob: P.append(f"em dashes in prose: {blob.count('—')}")
    words = sum(len(t.split()) for s in secs for t in s.get("reading", []))
    N.append(f"{len(secs)} sections, {words} words of reading, {len(ch.get('figureFiles', []))} figures, {len(its)} interactives")
    print("PROBLEMS" if P else "OK: no problems"); [print("-", x) for x in P]
    print("NOTES"); [print("-", x) for x in N]
    return 1 if P else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
