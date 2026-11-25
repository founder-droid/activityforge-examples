/**
 * ActivityForge — JavaScript example
 *
 * Generates a real word search through the ActivityForge API on
 * RapidAPI and prints it. No dependencies — Node 18+ (built-in fetch).
 *
 * Setup:
 *   1. Subscribe (free tier is fine) on the RapidAPI listing:
 *      https://rapidapi.com/aerolyf-global-holdings-llc-aerolyf-global-holdings-llc-default/api/activityforge
 *   2. Copy your key from the listing's Endpoints page.
 *   3. Run:  RAPIDAPI_KEY=your_key_here node generate.js
 */

const HOST = "activityforge.p.rapidapi.com";

async function generateWordSearch() {
  const res = await fetch(`https://${HOST}/v1/word-search`, {
    method: "POST",
    headers: {
      "X-RapidAPI-Key": process.env.RAPIDAPI_KEY,
      "X-RapidAPI-Host": HOST,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      theme: "ocean", // animals, space, garden, food, weather, farm,
      // jungle, arctic, school, sports, music — or send "words": [...]
      age_band: "6-8", // "3-5" | "6-8" | "9-12"
      seed: 42, // same seed = same puzzle, forever
      format: "all", // "json" | "svg" | "pdf" | "all"
    }),
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error(`ActivityForge ${res.status}: ${err?.error?.message ?? "request failed"}`);
  }
  return res.json();
}

const puzzle = await generateWordSearch();

console.log(`Word search — theme: ${puzzle.theme}, ages ${puzzle.age_band}, seed ${puzzle.seed}\n`);
for (const row of puzzle.grid) console.log(row.split("").join(" "));
console.log("\nFind these words:", puzzle.words.join(", "));
console.log("\nThe response also carries:");
console.log("  solution  — every word's start/end coordinates (the answer key)");
console.log("  svg       — a print-ready page (format 'svg' or 'all')");
console.log("  pdf_base64 — a vector PDF, base64-encoded (format 'pdf' or 'all')");
