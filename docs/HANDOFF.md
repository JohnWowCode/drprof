# Dr. Professor handoff

Branch: `claude/dr-professor-brainstorm-byp1ui` (repo johnwowcode/drprof). App: one file,
`app/dr-professor.html`, published as John's private artifact
https://claude.ai/artifact/9LQ9AcZVtv1tMjtTuWq1cW (capabilities sample, db, downloads, user; republish
without `capabilities` to keep them). Books live in the artifact's db: `courses/<id>` and
`courses/<id>/chapters/ch<n>`; reader progress is private under `data/users/<uid>/`.

## Where things stand (October 2026)

- 4 books with authored, fact-checked chapters: Birds ch1-4, Game Design ch1-2, Outer Space ch1-2
  (with SpaceEngine follow-alongs), Energy and Power ch1-2. Live in the app.
- 19 new course plans (syllabus, book bible with `canon` = the standard texts each course follows,
  preface, cover) in `app/seed/plans/`, merged into `app/seed/courses.json`. Their chapters are not
  written yet; the app can write a chapter on demand, but the authored pipeline below is better.
- Audiobook player plays recorded tracks (`chapter.studio.tracks[{label,text,src}]`); narration scripts
  are in `app/seed/books/<course>/ch<n>.narration.json`. Recording is waiting on John (see below).

## The authored-chapter pipeline

1. Writer agent writes `app/seed/books/<course>/ch<n>.json` + `ch<n>-fig-<k>.svg` per
   `docs/CHAPTER_SPEC.md`, following the course bible and its `canon`, and reading earlier chapters for
   continuity. `python3 scripts/validate_chapter.py <file>` must print OK.
2. A second, independent agent fact-checks it and writes `ch<n>.check.json` (template prompt: see the
   verifier prompts used for the first ten chapters; blind re-solve of every answer key, every source
   and figure label checked).
3. `python3 scripts/apply_check.py <chapter>`; re-validate; render figures with
   `PWPATH=$(npm root -g)/playwright node scripts/render_svgs.js out.png a.svg ...` and look.
4. `python3 scripts/build_seed.py`, test in a browser (Playwright, phone 390px and desktop 1280px),
   then write the docs to the artifact db with ArtifactData `batch` (pin `if_version` on existing docs;
   back up any chapter John generated himself before overwriting it, as in `app/seed/backup/`).
5. Commit and push.

Web search is shared across all agents in one turn (about 200 searches), so run about 8 writers at a
time.

## Waiting on John

- **Narrator voice** for studio audiobooks via his Higgsfield account (ElevenLabs engine, about 500
  credits for the first ten chapters, price-checked, nothing spent). Or allow `huggingface.co` for the
  free Kokoro voice.
- **Scholar connector** deploy on Vercel (needs his yes).
- **Network**: in a cloud session, the scholarly sites below are blocked unless added under Network
  access, Allowed domains (or a broader access level). A session running on John's own PC (Claude
  Desktop app opened on a local clone of this repo) has no such limit and can also write JDo reports
  straight into `C:\Users\johnw\Documents\WowCool Game Builds\JDo\data\inbox\`.

### Domains worth allowing

- Scholarly: api.openalex.org, api.crossref.org, doi.org, api.semanticscholar.org, arxiv.org,
  export.arxiv.org, eutils.ncbi.nlm.nih.gov, pubmed.ncbi.nlm.nih.gov, openlibrary.org, archive.org,
  en.wikipedia.org, www.wikidata.org, plato.stanford.edu, iep.utm.edu
- Physics: pdg.lbl.gov, inspirehep.net, home.cern, physics.nist.gov
- Religion and ancient texts: www.vatican.va, bible.usccb.org, www.ccel.org, www.perseus.tufts.edu,
  etcsl.orinst.ox.ac.uk, cdli.earth
- Museums: www.britishmuseum.org, collectionapi.metmuseum.org, www.cmog.org
- Dinosaurs: paleobiodb.org
- Food and safety: fdc.nal.usda.gov, api.nal.usda.gov, www.fsis.usda.gov, www.fda.gov
- Fungi: www.mycobank.org, api.inaturalist.org, mushroomobserver.org
- Money: www.investor.gov, www.sec.gov, fred.stlouisfed.org
- Games: partner.steamgames.com, store.steampowered.com, www.gdcvault.com, spaceengine.org
- Health: www.cdc.gov, health.gov, www.who.int
- Voices: huggingface.co

## Rules John set

One teacher (Dr. Professor) per book, coherent across chapters; accuracy first (false premises are
taught as claims versus evidence); writing must never read as AI; no publishing, deploying, spending
or paid APIs without John's yes to that exact action in the session; ask before deleting files; never
write to Frog's Project Dashboard folder; report into JDo when stopping.
