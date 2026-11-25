# ActivityForge Examples

Runnable examples for the **ActivityForge API** — generate print-ready
kids' activity puzzles (word searches, mazes, dot-to-dots) with verified
answer keys, as JSON, SVG, and PDF.

**Get a free key:** subscribe to the free BASIC plan (100 calls/day) on
the RapidAPI listing and copy your key from the Endpoints page:
https://rapidapi.com/aerolyf-global-holdings-llc-aerolyf-global-holdings-llc-default/api/activityforge

## Examples

- [`javascript/`](javascript/) — Node 18+, zero dependencies
- [`python/`](python/) — Python 3, uses `requests`

Each example generates a real ocean-themed word search (ages 6-8,
seed 42) and prints the grid, the word list, and what else the response
carries (solution coordinates, SVG page, base64 PDF).

## Endpoints

| Method | Path | What it makes |
|---|---|---|
| GET | `/v1/themes` | The 12 themes, 8 shapes, age bands, difficulties |
| POST | `/v1/word-search` | Word search from a theme or your own word list |
| POST | `/v1/maze` | Maze by difficulty or exact grid size, with solution |
| POST | `/v1/dot-to-dot` | Dot-to-dot from 8 original silhouettes |
| POST | `/v1/activity-page` | Themed activity set + answer keys, one PDF |

Custom word lists pass a child-safety screen. Same `seed` = same
puzzle, regenerated exactly, forever.

Built by AeroLyf Global Holdings LLC. All wordlists and puzzle designs
are original content.
