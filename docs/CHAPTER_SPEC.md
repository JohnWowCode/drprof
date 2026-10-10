# Chapter specification (seed books)

A chapter is one JSON file `app/seed/books/<course-id>/ch<N>.json` plus 2-4 SVG figures `ch<N>-fig-<K>.svg` in the same folder. `scripts/validate_chapter.py` must report no problems. The reference chapter is `app/seed/books/birds-beginner-seed/ch1.json`.

## The teacher
One author, **Dr. Professor**: a world-class expert in the subject with deep and wide knowledge of its history, evidence, methods and open questions, who is also a gifted, engaging teacher. Every important claim shows how we know it, then what follows from it. Clear, warm and direct, never chatty or padded. The book's `bible` in `app/seed/courses.json` (teacher stance, promise, threads, running examples, conventions) must be followed so all chapters read as one coherent book. Refer back to earlier chapters by number and use the running examples.

## Writing rules
- Accuracy first: only well-established facts, each checked against a reliable source. No invented numbers, studies, quotes, dates or names. Round or omit what you cannot confirm. Distinguish consensus from open debate.
- Match the course level (Noob, Beginner, Intermediate, Advanced, Expert, Mastery) in vocabulary and depth; simpler never means less accurate.
- No stock AI phrasing (the validator lists banned phrases), no em dashes, no rhetorical-question openers, no summarizing morals at paragraph ends. Vary sentence length. Concrete nouns, real numbers, named examples.
- Inside strings: `**bold**` for a key term's first use, `*italic*` for emphasis and scientific names; nothing else. Use ’ and “ ” typographic quotes inside JSON strings rather than escaped straight double quotes.

## JSON shape
```json
{
  "n": 2,
  "figureFiles": [ { "section": "2.1", "file": "ch2-fig-1.svg", "caption": "1-2 sentences: what to notice" } ],
  "lesson": {
    "hook": "Opening paragraph (80-150 words): a real puzzle, event or surprising fact that makes the reader want the chapter; true and verifiable.",
    "overview": "One paragraph: what the chapter covers and how it connects to earlier chapters.",
    "objectives": ["3-5, each starting with a verb"],
    "sections": [ {
      "n": "2.1", "title": "exactly as in the syllabus",
      "reading": ["4-6 paragraphs, 80-170 words each, with citation markers like [1] or [1, 2] before the final period of sentences making important factual claims"],
      "sources": [ { "n": 1, "citation": "Full APA 7 reference; DOI as https://doi.org/... only if you saw it on the publisher, Crossref or PubMed page", "kind": "article|book|chapter|report|website", "supports": "the claim it supports" } ],
      "keyTerms": [ { "term": "...", "def": "one sentence" } ],
      "example": { "title": "Worked example: ...", "steps": ["3-6 steps"], "takeaway": "one sentence" },
      "misconception": { "myth": "how people actually say it", "fact": "correction and why" },
      "practice": [
        { "type": "mc", "q": "...", "choices": ["4 choices"], "answer": 0, "explanation": "why right, why others wrong" },
        { "type": "short", "q": "...", "answer": "model answer", "explanation": "what a good answer includes" }
      ]
    } ]
  },
  "interactives": [ "2-4 items, see below" ],
  "assess": {
    "slides": [ { "title": "...", "bullets": ["3-5"], "notes": "2-4 sentences" } ],
    "quiz": [ { "sec": "2.1", "q": "...", "choices": ["4"], "answer": 0, "explanation": "..." } ],
    "challenge": [ { "title": "...", "prompt": "2-5 sentences", "deliverable": "typed text the learner submits", "rubric": ["3-5 criteria"] } ],
    "readings": [ { "citation": "APA 7", "kind": "book|chapter|article|report|website", "why": "what to read it for", "pages": "" } ],
    "videos": [ { "search": "YouTube search query", "why": "what to watch for" } ],
    "images": [ { "search": "image search query", "source": "wikimedia|nasa", "why": "what to look for" } ]
  }
}
```
Counts: sections exactly as the syllabus; 2-5 sources and 3-6 key terms per section; exactly 3 practice problems per section (mix mc and short; at least one applies the idea to a new case); 8-12 slides (first is the agenda, last the summary); exactly 8 quiz questions spread across all sections, at least 3 requiring application, answer positions varied; exactly 2 challenges; 3-5 readings; 2-3 videos; 2-3 images. All answer indexes are 0-based.

Sources: academic standing only (peer-reviewed journals, university-press or standard academic texts, scientific agencies such as NASA, NOAA, USGS, IEA, IPCC, national academies, major museums and learned societies). Never Wikipedia, blogs or news. Verify every citation exists with exactly these details.

## Figures (SVG)
`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480">`, first child `<rect width="800" height="480" fill="#ffffff"/>`, a title at top left (font-size 18). Text uses `font-family="Helvetica, Arial, sans-serif"`, font-size 14-18. Full color with meaning: blue #2E6DA4/#BBD5EE, green #2F7D4F/#C4E3C9, orange #C8691C/#F6D2AE, red #B0303A/#F2C4C8, purple #6B4FA0/#DCD2EE, ochre #A0781A/#EFE0B4, grays #444444/#DDDDDD; light fills with matching dark outlines; label text colored to match its part. Labels never overlap shapes or each other; leader lines to parts. Use the field's standard conventions (ICS period colors, circuit symbols, axis conventions). Say "not to scale" when it isn't. No script, image, foreignObject, style, filters or external links. Render with `scripts/render_svgs.js` and look before finishing.

## Interactives (built-in components; you supply only data)
Every item has `"type"`, `"section"` (e.g. "2.1"), `"title"`, `"intro"` (what to try or notice).
- **explorer**: sliders drive formulas. `"inputs": [ { "id": "v", "label": "Airspeed", "unit": "m/s", "min": 0, "max": 30, "step": 0.5, "value": 10 } ]`, optional `"constants": { "rho": 1.225 }`, `"outputs": [ { "label": "Lift", "unit": "N", "expr": "0.5*rho*v^2*S*CL", "digits": 1 } ]`, `"takeaway"`. Expressions may use numbers, input ids, constants, `pi`, `e`, `+ - * / ^`, parentheses and `sqrt abs sin cos tan log log10 exp min max pow round floor ceil` (log is natural; trig in radians). Physically correct formulas only, with realistic ranges.
- **sort**: `"buckets": ["Bird", "Not a bird"]`, `"items": [ { "text": "...", "bucket": 0, "why": "..." } ]` (6-10 items).
- **order**: `"steps": ["in the correct order", ...]` (4-7), `"explain"`.
- **timeline**: `"unit": "million years ago"`, `"reverse": true` if larger numbers are earlier, `"events": [ { "t": 150, "label": "...", "detail": "..." } ]` (5-9).
- **scale**: `"unit": "grams"`, `"log": true|false`, `"items": [ { "label": "...", "value": 2.0, "note": "..." } ]` (4-8, real values).
- **case**: a think-then-reveal showcase. `"intro"` sets a real scenario; `"steps": [ { "q": "question to think about", "a": "the answer and reasoning" } ]` (2-4).

### Follow-along in an outside app (`sim`)

An optional extra beside the 2-4 interactives, for following the chapter inside a real program the
reader runs (first: SpaceEngine for the Outer Space book). It never replaces an in-page interactive,
and the chapter must make complete sense without it.

```json
{ "type": "sim", "section": "1.2", "app": "SpaceEngine", "title": "Watch a month of Moon phases in an hour",
  "intro": "why this is worth doing in the simulator",
  "setup": "what to have open first (optional)",
  "steps": [ { "do": "one concrete action, naming the real menu, panel or key", "see": "what the reader should now see" } ],
  "notice": "the takeaway once all steps are done",
  "check": { "q": "question answered from what they saw", "choices": ["..", ".."], "answer": 0, "why": ".." } }
```
Rules: 3-8 steps. Every control, menu name and key must be verified against the app's own manual or
documentation; where it cannot be verified, describe the goal in words ("open the search panel and find
the Moon") instead of naming a key. Never claim the simulator is a source of fact; it illustrates what the
chapter's cited sources say.
