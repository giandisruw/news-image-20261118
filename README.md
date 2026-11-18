# news-image-20261118 — "THE WORLD", Wednesday 18 November 2026

A one-page newspaper front page summing up the world's news of
Wednesday 18 November 2026, drawn with PIL and stored as `entry.png`.

## The image

- **Lead — Crimea bridge arch collapses in Ukrainian strike.** Kyiv says
  Neptune missiles and Palianytsia drones destroyed the road arch in a
  seven-stage operation; Moscow confirms damage and halts traffic. Russia
  says it downed 1,441 drones — its largest drone tally of the war.
- **Iran drones target US radar in Bahrain.** Tehran's third strike in
  days on US targets in the Gulf kingdom; Bahrain says the drones were
  intercepted, the US reports no damage and no injuries.
- **Trump lands in Manila for Quad talks.** First Quad leaders' meeting in
  two years. On Wednesday he meets President Marcos, then heads to
  Shenzhen for APEC and a planned meeting with Xi Jinping and Putin.
- **Hormuz tanker hit twice; one sailor missing.** LPG carrier Tara Gas
  attacked on 16–17 Nov; the crew abandons ship, 21 Indians evacuated
  to Oman.
- **Knesset picks Eisenkot ally as speaker.** Matan Kahana wins 66–52, a
  blow to Netanyahu after October's deadlocked election. Britain sanctions
  eight settlement firms over the E1 tender.
- **Cyclone Akvan heads for Andhra coast.** Severe storm in the Bay of
  Bengal; landfall forecast Fri 20 Nov, winds 120–130 km/h.
- **Dhoni retires from the IPL.** CSK great, 45, ends a 19-year career
  with five titles; stays on as team mentor for 2027.
- **Also today:** Canada–China trade deals as Xi meets Carney; Amazon's
  $7bn Indian renewables investment; India re-elected to the ITU Council.

## Files

- `main.py` — Python 3.13, standard library only. Copies the bundled
  `entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`).
  No network, no randomness: both grader runs write identical bytes.
- `entry.png` — the front page, 1024×1024 PNG.
- `build_image.py` — the PIL script that drew `entry.png` (run it to
  regenerate the image; it needs only PIL and the Liberation fonts).
- `NOTES.md` — research notes and sources for every story.
- `LICENSE` — MIT.

## Timing note

This entry was built at about 00:20 UTC on Wed 18 Nov 2026, when the news
day had barely started. Its stories are the overnight 17–18 Nov reports
plus the major developing stories carried over from 17 Nov that are still
the day's news (see NOTES.md). A later resubmission with fuller 18 Nov
news is possible before the Fri 20 Nov 2026 07:00 WIB / 00:00 UTC deadline.
