# ActivityForge — JavaScript example

Generate a real, print-ready word search (with a verified answer key)
from the [ActivityForge API](https://rapidapi.com/aerolyf-global-holdings-llc-aerolyf-global-holdings-llc-default/api/activityforge)
in about 30 lines of dependency-free Node.js.

## Run it

```bash
# 1. Get a free key: subscribe to the free BASIC plan on the listing,
#    then copy your key from the Endpoints page.
# 2. Run:
RAPIDAPI_KEY=your_key_here node generate.js
```

Requires Node 18+ (uses the built-in `fetch`).

## What you get back

- `grid` — the letter grid (array of strings)
- `words` — the words to find
- `solution` — every word's start/end coordinates (the answer key)
- `svg` — a print-ready page (with `format: "svg"` or `"all"`)
- `pdf_base64` — a vector PDF (with `format: "pdf"` or `"all"`)

## Make it yours

Change `theme` (12 built in: animals, ocean, space, garden, food,
weather, farm, jungle, arctic, school, sports, music), `age_band`
("3-5", "6-8", "9-12"), or send your own `words` list instead — custom
words pass a child-safety screen. Same `seed` = same puzzle, every
time. Other endpoints: `POST /v1/maze`, `POST /v1/dot-to-dot`,
`POST /v1/activity-page`, `GET /v1/themes`.
