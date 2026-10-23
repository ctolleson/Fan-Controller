# Fan controller passdown

Updated 2026-10-22 after resuming the requested DRC/ERC repair.

## Current result

**Native KiCad 10.0.6: ERC 0, DRC 0, unconnected 0, courtyard violations 0.** Schematic-to-PCB transfer is **63/63 named pad nets**; footprint parity **22/22**. No exclusions or relaxed severities were added in this repair. Native reports retain existing default/project ignored-check lists.

The previous unvalidated 226-finding checkpoint is superseded. Its passdown is archived at `KiCad/fancontroller/recovery/final_drc_repair/PASSDOWN_before_revalidation.md`.

**The aggregate MCP project gate remains FAIL**, with the exact report preserved. It mistakes pinless H1–H4 mounting-hole symbols for isolated electrical symbols, and its placement heuristic ignores footprint rotation and origin offsets. A separate read-only geometric audit of all 22 actual transformed courtyard polygons finds no overlaps; J1/P1 are inside the outline. J2's courtyard extends 0.006 mm past the outline; native copper edge clearance passes. This is not a waiver or proof of actual purchased connector/mating-cable fit. Schematic cosmetics remain advisory (32/100), with text overlap in the working PDF.

## User scope and authority

- Five PCBs, top-side SMT assembly; connectors J1/J2 and external-pot header P1 hand assembled.
- User approved stocked replacements and confirmed **12 V supply**.
- Bare PCB + one **150 × 150 mm frameless top-side paste stencil + shipping** is a separate requested quote option. Save quotes in JLCPCB.
- No purchase/payment authorized or made. No new vendor quote was obtained in this repair turn.

## Repairs completed

All CAD changes were made with dedicated registered KiCad MCP tools, not raw schematic/PCB rewrites.

- Removed dangling DUTY_REF trace and two zero-length tracks.
- Replaced C2/C4 with exact project-local legacy footprints at 270°, removing tiny geometric mismatch warnings.
- Moved colliding reference fields to Fab and added legible native board references, 12 V input polarity, fan pin labels and board ID. Preserved pin-1 and C5 polarity markings. Rendered and inspected final board.
- Added **C6, 100 nF / 25 V**, REG1 input-to-ground bypass, per KF50 application guidance. Same part as C2/C3: KEMET C0603C104K3RALTU, LCSC C2167748. Routed input and ground via, refilled zone, saved board. Assembly is now **15 SMT parts/board**, still 11 grouped BOM rows.
- Normalized schematic power orientations and autoplaced fields. ERC remains clean; drawing still needs cosmetic cleanup if a polished schematic is required.
- Regenerated Gerbers, drill, netlist, native positions, rotation-corrected CPL, vendor BOM, previews and reports from the repaired project.

Selected substitutions remain REG1 KF50BD-TR C222151 (20 V input maximum), C1 C577166, C4 C113888, C5 C336786. C5's 2000 h at 105°C rating versus original 5000 h remains disclosed. Original 12–28 V silk is replaced by 12 V.

## Revised artifacts — authoritative candidate

Directory: `/Users/ctolleson/Documents/Claude/PWM_Fan_Controller/KiCad/fancontroller/release_12v`

Read its **README.md** for full findings and upload instructions.

- `fancontroller_12v_gerbers_DRAFT.zip`: new repaired Gerbers/drills, including silk and paste.
- `BOM.csv`: 11 rows / 15 SMT parts.
- `CPL.csv`: same 15 refs, Top, mm, native negative-Y absolute Gerber frame; SOIC offsets applied and angles normalized.
- `erc_report.json`, `drc_report.json`: native clean reports.
- `project_quality_gate.json`: full FAIL result, not suppressed.
- `placement_geometry_review.json`: all 22 actual courtyard polygons, rotated/translated, no overlaps.
- `validation_summary.json`, `assembly_audit.json`, `SHA256SUMS`.
- `board_preview.png`, `board.pdf`, `schematic.pdf` (working drawing with readability defects).

**macOS case-insensitive filesystem:** do not export another lowercase `bom.csv` into that directory; it would overwrite vendor `BOM.csv`. Root workbook and root draft placement CSV are historical and omit C6/final repairs. `JLCPCB_Quote/` preserves old prices/uploads only.

## Remaining before an order

1. Review actual hand-assembled connector fit and mating clearance. J1 uses official KiCad Molex-compatible fan header (Molex 47053-1000); J2 is a generic 2.54 mm 1×2 power header; P1 is a generic 1×3 header for an external potentiometer. Official J1 library drills are 1.02 mm signal/1.1 mm locating hole; original Gerber holes were slightly larger. P1/J2 use 1.0 mm holes.
2. Upload the **new** ZIP/BOM/CPL to JLCPCB, quote five boards/15 SMT parts, refresh stock, inspect the new matched-part preview (SOIC pin 1 and C5 polarity especially), and save the quote. The separate 150 mm paste stencil quote must also use the new artwork.
3. Obtain vendor DFM and human engineering review. No bench testing or simulation was performed. Clean ERC/DRC does not prove functional performance.
4. Do not represent the aggregate MCP gate as passed. Its mechanical/placement implementation issues and schematic readability advisory are explicitly preserved in the candidate README.

## Historical saved JLCPCB quotes — original artwork only

Cart: https://cart.jlcpcb.com/shopcart/cart/

- **Y23-8373413A**, `fancontroller_original_gerbers_Y23`: five boards USD 4.10 + 150 × 150 mm frameless top stencil USD 7.22 = **USD 11.32 merchandise**. Estimated DHL Express DDP shipping USD 31.59 gives **USD 42.91 before additional checkout tax**. Shipping was an estimate, not locked by cart save.
- Stencil reference SO12610230396-8373413A.
- Saved editor: https://cart.jlcpcb.com/shopcart/cartEdit/?id=523bfaf9478e4e31b322796c3e1a8a81&type=1&changeType=2&achieveDate=48
- **Y21**, original five-board/14-SMT build: PCB USD 4.00 + PCBA USD 55.91 = **USD 59.91 before shipping/tax**. PCBA includes setup 8.24, assembly stencil 1.55, parts 13.64, extended fees 30.90, placement 0.67, nitrogen 0.91.
- **Y22** is a separate 380 × 280 mm stencil alternative, left intact. Avoid checking out duplicate alternatives.
- All prior saved quotes use the unchanged original Gerber ZIP. They do **not** price this revised C6/15-part board. Records remain in `JLCPCB_Quote/`.

## Git and MCP runtime

Project root: `/Users/ctolleson/Documents/Claude/PWM_Fan_Controller`.
Branch: `feature-kicad-project-bom`; authorized origin: `https://github.com/ctolleson/Fan-Controller.git`.
Restore tag for this turn: `checkpoint-before-final-drc-repair`. Prior checkpoint commit: 56da39c. See git log for the repair/release commit. Follow user commit-and-push discipline.

KiCad project: `KiCad/fancontroller/fancontroller.kicad_pro`, `.kicad_sch`, `.kicad_pcb`. Project-local legacy footprints: `Recovered2018.pretty`; regulator symbol: `custom_symbols.kicad_sym`. Original inputs `Gerber/`, drill files and schematic images are unchanged.

MCP source checkout: `/Users/ctolleson/Documents/Claude/KiCad-MCP-Pro-Improvements/kicad-mcp-manufacturing-runtime.nosync`.
Python: `/Users/ctolleson/Documents/Claude/KiCad-MCP-Pro-Improvements/venv.nosync/bin/python`.
MCP version 3.34.0, native CLI 10.0.6. MCP branch `feature-runtime-footprint-placement`, authorized private remote `https://github.com/ctolleson/kicad-mcp-pro-private.git`; last prior source fix e100c9e. No MCP source edits in this repair turn.

Chat MCP IPC reports unavailable due to the wrong default socket. Fresh local full-profile MCP reaches the PCB Editor via `KICAD_API_SOCKET=ipc:///private/tmp/kicad/api-55365.sock` (process-specific; rediscover on resume). Use `PYTHONPATH=src`, `KICAD_MCP_PROFILE=full`, `KICAD_MCP_OPERATING_MODE=write` from that source checkout and the registered-tool runner `recovery/call_local_mcp.py`. File-backed edits do not reload a GUI board: save live edits first, then use `pcb_revert` to reload intentional file changes before more live operations. Never save stale GUI state over corrected files.

Recovery requests/results are copied under `recovery/final_drc_repair/`. **Do not replay historical mutation batches.** Dedicated read-only `recovery/audit_release_geometry.py` uses sexpdata and Shapely for the transformed-courtyard audit.

Known MCP defects:

- `pcb_set_design_rules` previously generated invalid non-native .dru syntax. Do not use it; `pcb_apply_manufacturer_rules` was used instead. Invalid generated file is outside the project in `/private/tmp/fan-invalid-generated-rules.kicad_dru`.
- Placement heuristic ignores rotation/offset and flags valid pinless mounting holes in connectivity checks.
- Live DFM counts 3 copper layers incorrectly; saved board and outputs have only F.Cu/B.Cu. Stackup helper sums surface layers; native board thickness is 1.6 mm. Live DFM measured track minimum 0.160 mm, via drill 0.399 mm, DRC/unconnected/courtyard/silk-overlap hints all 0. Generic manual review warning persists.
- `export_pick_and_place` failed; official `kicad-cli pcb export pos --format csv --units mm --side front --smd-only --exclude-dnp` produced the 15-part native export. MCP rotation correction then succeeded.

Chrome is signed into JLCPCB, but extension file uploads remain blocked despite Allow access to file URLs. User manual uploads previously worked. Do not repeatedly request the same permission toggle. Reinitialize browser documentation and inspect current tabs before continuing quote work; no browser action was taken in this repair turn.
