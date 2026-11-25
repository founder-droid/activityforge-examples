"""ActivityForge — Python example.

Generates a real word search through the ActivityForge API on RapidAPI
and prints it.

Setup:
    1. Subscribe (the free tier is fine) on the RapidAPI listing:
       https://rapidapi.com/aerolyf-global-holdings-llc-aerolyf-global-holdings-llc-default/api/activityforge
    2. Copy your key from the listing's Endpoints page.
    3. pip install -r requirements.txt
    4. RAPIDAPI_KEY=your_key_here python generate.py
"""

import os
import sys

import requests

HOST = "activityforge.p.rapidapi.com"


def generate_word_search() -> dict:
    response = requests.post(
        f"https://{HOST}/v1/word-search",
        headers={
            "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
            "X-RapidAPI-Host": HOST,
            "Content-Type": "application/json",
        },
        json={
            "theme": "ocean",  # or send "words": [...] with your own list
            "age_band": "6-8",  # "3-5" | "6-8" | "9-12"
            "seed": 42,  # same seed = same puzzle, forever
            "format": "all",  # "json" | "svg" | "pdf" | "all"
        },
        timeout=30,
    )
    if not response.ok:
        try:
            message = response.json()["error"]["message"]
        except Exception:
            message = "request failed"
        sys.exit(f"ActivityForge {response.status_code}: {message}")
    return response.json()


def main() -> None:
    if "RAPIDAPI_KEY" not in os.environ:
        sys.exit("Set RAPIDAPI_KEY first — see the docstring at the top of this file.")

    puzzle = generate_word_search()

    print(f"Word search — theme: {puzzle['theme']}, "
          f"ages {puzzle['age_band']}, seed {puzzle['seed']}\n")
    for row in puzzle["grid"]:
        print(" ".join(row))
    print("\nFind these words:", ", ".join(puzzle["words"]))
    print("\nThe response also carries:")
    print("  solution   — every word's start/end coordinates (the answer key)")
    print("  svg        — a print-ready page (format 'svg' or 'all')")
    print("  pdf_base64 — a vector PDF, base64-encoded (format 'pdf' or 'all')")


if __name__ == "__main__":
    main()
