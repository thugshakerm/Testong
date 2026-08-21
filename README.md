# ROBLOX 2014 Avatar Editor — Pixel Recreation

A 1:1 recreation of `B0CSUKJCMAAVIq9.webp` — the **ROBLOX Android app's
avatar editor (October 2014)** — as a single static page.

**Open:** [`recreation/index.html`](recreation/index.html)

## What it is

- The screenshot is the ROBLOX **Android app** avatar/customize screen, not
  the website (confirmed by the user).
- Per the request, the **avatar figure**, the **outfit-tile mini figures** and
  the **worn-item mini figures** are intentionally left **blank** — only the
  UI chrome is reproduced.
- Website navbar assets are used for reference (the saved 2014 HTML pages in
  the repo root were used for research).

## How it was analyzed (no vision — pure math)

Everything was reverse-engineered from the raster itself:

- **OCR** (RapidOCR, multi-scale upscaling) for all text.
- **Pixel-by-pixel** luma/saturation maps to locate every element.
- **Connected-component / run-length scans** to measure exact bounds,
  colors, gaps, strokes and the palette grid geometry.
- **Glyph-shape tracing** of tiny unreadable text (e.g. the truncated outfit
  name "RobloxUnver..." and the 9px item names were read from the glyph
  pixels).
- Cross-referenced the saved Wayback Machine MHTML pages (Jan 2014 +
  Dec 2014 + Style Guide) for the era's font and navbar.
- **Font research:** the 2014 ROBLOX website CSS declares
  `font-family: "Source Sans Pro", Arial, Helvetica, sans-serif` — used here
  (Google Fonts) with Roboto/Arial fallback.
- Geometric verification: every non-text element was painted from the
  recreation's coordinates with PIL and diffed against the original
  (dividers ~0.1 mean error, hairline/pill ~2-6, palette ~10 incl. AA).

## Key measurements (screenshot 680×510)

| Element | Position / spec |
|---|---|
| Stage bg | white + Android status-bar scrim: `#F7F7F7` band y0-24 fading to white ~y44 |
| Menu icon | 3×3 grid of 4px squares `#050C38`, x13-26 y8-20 |
| Logo mark | small gray blob `#ADADAD` (pixel-traced SVG), x31-52 y6-23 |
| Gray pill | x277-334 y29-34, `#D3D3D3` |
| Navbar hairline | y33, x373-659, `#E0E0E0` |
| Robux coin | tilted ellipse + `R$` glyph `#2E6E3C`, x529-546 y9-19 |
| Ticket icon | tan `#E8D9AE` w/ orange band `#D98E55`, x596-609 y8-20 |
| Amounts | `91`, `12` — 13px semibold `#6E6E6E` |
| Left links | "Something wrong with your Avatar?" `#8A8A8A`, "Click here to re-draw it!" `#6D7E90`, 13px |
| Enable 3D chip | x227-264 y262-275, border `#E9E9E9`, text 9px `#606060` |
| Avatar Colors | 17px bold `#1F1F1F` |
| Hint | "Click a body part to change its color:" 13px `#6C6C6C` |
| Palette | `#FFCC99` circles Ø31 staggered grid (11 visible incl. partials) |
| Create New Outfit | x583-655 y57-75, border `#E5E5E5` r8, text 11px `#2E2E2E` |
| Outfit names | 11px semibold `#353535` (Hallow, Racer, The Dark One, Deadman / RobloxUnver..., SliverMan, oldmAn, MrZombie) |
| Created: / dates | 11px `#ADADAD` / 10px `#828282` (10/13/2014, 10/5/2014, 10/4/2014, 9/16/2014, 9/10/2014, 9/5/2014, 9/5/2014, 8/20/2014) |
| Pagination | chips x424/x500 + "Page 1 of 2" 12px `#505050` |
| Divider | 2px (y374 `#E5E5E5` + y375 `#F1F1F1`) x260-639 |
| Currently Wearing | 20px bold `#202020` |
| Remove buttons | 4× 35×17 glossy blue gradient, "Remove" 9px bold `#0B3172` |
| Item names | 9px `#758A9E` (ZombieFad, Ghost Factor, Halloween Adidas, JackOLantern) |
| Online chip | x627-675 y492-509 solid `#D6D6D6` r8, green dot `#1C8121→#2E9E41`, "Online" 10px bold `#141414` |

## Files

- `recreation/index.html` — the recreation
- `recreation/style.css` — all styles
- `_analysis/` — extraction + verification scripts and decoded assets
