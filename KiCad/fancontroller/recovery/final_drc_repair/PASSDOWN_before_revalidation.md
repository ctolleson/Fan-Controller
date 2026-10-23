# Fan controller passdown

Updated: 2026-10-22, approximately 18:35 America/Denver (2026-10-23 00:35 UTC).

**Stopped at the user's explicit request: “write a PASSDOWN.md and stop here.” Do not resume design work until requested.**

## Goal and authorization

Recover an editable KiCad project from the supplied Gerbers, drill files, BOM and schematic image; repair footprint, ERC and DRC issues; obtain a JLCPCB quote with silkscreen, BOM and placement data. User selected **5 boards, SMT assembly**, authorized stocked substitutions, and confirmed **12 V supply**. Connectors and external potentiometer are for hand assembly. The latest quote request is a separate **bare PCB + solder-paste stencil + shipping** option. User requires quotes to be saved in JLCPCB.

No purchase has been made. The saved vendor quotes use the **original Gerber ZIP**, not the PCB reconstruction currently being repaired. Do not order the repaired design using those old uploads.

## Saved JLCPCB quotes

Cart: https://cart.jlcpcb.com/shopcart/cart/

### Bare PCB plus solder-paste stencil — saved and verified

Cart item: **fancontroller_original_gerbers_Y23**.

| Item | USD |
| --- | ---: |
| Five green, 1.6 mm, HASL PCBs, white silkscreen included, deburring included | 4.10 |
| One frameless, top-side, **150 × 150 mm solder-paste stencil** | 7.22 |
| Merchandise total saved in cart | **11.32** |
| DHL Express DDP shipping estimate, 2–4 business days | 31.59 |
| Estimated total before any additional checkout tax | **42.91** |

PCB reference: `Y23-8373413A`. Stencil reference: `SO12610230396-8373413A`.

Saved editor URL: https://cart.jlcpcb.com/shopcart/cartEdit/?id=523bfaf9478e4e31b322796c3e1a8a81&type=1&changeType=2&achieveDate=48

The cart visibly shows the 150 × 150 mm stencil and USD 11.32 merchandise total. USD 31.59 shipping was obtained from the instant quote with equivalent compact-stencil settings; shipping is an estimate, not locked by saving the cart. Checkout tax was not finalized. Do not represent USD 42.91 as a paid or final invoice total.

Records: `JLCPCB_Quote/pcb_stencil_quote.json`, `pcb_stencil_saved_cart.png`, and `README.md`.

The cart also contains `Y22`, a separate five-board quote with a **380 × 280 mm** stencil. Do not accidentally select both PCB/stencil alternatives for checkout. It was left intact.

### Earlier five-board SMT assembly quote

Cart item: **fancontroller_original_gerbers_Y21**, Economic top-side PCBA, 14 SMT parts per board / 11 BOM lines.

| Item | USD |
| --- | ---: |
| Five PCBs | 4.00 |
| Assembly setup | 8.24 |
| Factory assembly stencil | 1.55 |
| Components, including attrition | 13.64 |
| Extended component fees | 30.90 |
| SMT assembly | 0.67 |
| Nitrogen reflow | 0.91 |
| PCBA subtotal | **55.91** |
| PCB + PCBA, before shipping/tax | **59.91** |

The USD 1.55 factory assembly stencil is not the separately shipped USD 7.22 manual paste stencil.

Earlier draft URL: https://cart.jlcpcb.com/smt-order/?pcbFileNo=30188cbaad6147518de35d540fbe1b3e . This URL did not restore the uploaded board correctly during this turn; use the saved **Y21 cart entry** to resume.

Records: `JLCPCB_Quote/quote_summary.json`, `quote_59_91.png`, `substitutions.json`, `BOM.csv`, `CPL.csv`. Stock and pricing must be refreshed before ordering.

## Git and source locations

- Project root: `/Users/ctolleson/Documents/Claude/PWM_Fan_Controller`.
- Branch: `feature-kicad-project-bom`.
- Authorized origin: `https://github.com/ctolleson/Fan-Controller.git`.
- `ea370ac` — schematic connections and zero-ERC evidence, already pushed.
- `c73f79a` — prior USD 59.91 assembly quote and selected replacements.
- `73b1099` — recovered original SMT footprints and pad geometry.
- Restore tag before this reconstruction: `checkpoint-before-electrical-reconstruction`.
- Current PCB work and this passdown are saved in the final passdown commit after `ea370ac`; see `git log` for its hash.

Follow the user's global Git workflow: meaningful commits, never leave task changes uncommitted, and push the branch. Existing project branch is the active repair branch. Create a new feature branch from the default branch for a new feature.

KiCad MCP source checkout in use:

`/Users/ctolleson/Documents/Claude/KiCad-MCP-Pro-Improvements/kicad-mcp-manufacturing-runtime.nosync`

Runtime Python:

`/Users/ctolleson/Documents/Claude/KiCad-MCP-Pro-Improvements/venv.nosync/bin/python`

MCP branch: `feature-runtime-footprint-placement`. User-authorized private remote: `https://github.com/ctolleson/kicad-mcp-pro-private.git` (remote name `private`; old origin was unavailable). Last prior pushed MCP fix: `e100c9e`, correct absolute pad angles when placing/moving footprints. No MCP source code was changed in this turn.

## Current KiCad state

Project: `KiCad/fancontroller/fancontroller.kicad_pro`, `.kicad_sch`, `.kicad_pcb`. KiCad CLI **10.0.6**, MCP **3.34.0**.

### Schematic completed in this turn

- Reconstructed the circuit using KiCad MCP pin stubs, power symbols and named nets. The starting schematic had 17 unwired symbols and ERC 79.
- Native ERC subsequently reported **zero findings**, with no new exclusions or severity changes. Evidence: `KiCad/fancontroller/validation/erc_reconstructed.json`.
- Replaced the all-passive TS2938 symbol with a generated project-local **KF50BD-TR SO-8** symbol containing correct electrical pin types. Pin 1 output, pins 2/3/6/7 ground, pin 4 NC, pin 5 INHIBIT grounded to enable, pin 8 input.
- Updated REG1, C1, C4 and C5 values/sourcing properties to the approved stocked quote selections.
- External supply PWR_FLAGs at J2 identify +12 V and ground.
- IC1 output/control, IC3 control/discharge, REG1 NC and J1 tach are intentionally unconnected.
- LM311 balance pins 5/6 are now **individually unconnected** instead of shorted. TI permits either unused configuration: https://www.ti.com/lit/ds/symlink/lm311.pdf . The short was omitted from recovered PCB copper as well.
- Added connector footprint assignments and four mechanical mounting-hole symbols **after** the saved zero-ERC report. Re-run ERC to verify the final schematic snapshot; the existing clean report predates those final mechanical additions.

### PCB reconstruction performed

The starting PCB was imported Gerber artwork: about 123,500 graphical shapes, 808 unnetted tracks and 29 pseudo-vias, overlaid by 14 recovered SMT footprints. Baseline DRC: **639**.

Through supported KiCad MCP operations:

1. Removed imported copper/mask/paste artifacts and pseudo-vias, retaining the original outline.
2. Added J1 fan header, J2 power header, P1 external-pot header and four actual 2.2 mm NPTH mounting-hole footprints.
3. Transferred **53 pad net assignments** and updated component values from the schematic.
4. Analyzed original Gerber geometry read-only with gerbonara + Shapely, cross-checked functional nets against the schematic image, then restored **206 native track segments** and 15 real vias through MCP.
5. Replaced the floating imported bottom copper artwork with a native **GND B.Cu zone**, 0.2 mm clearance/minimum width, thermal gap/spoke width 0.3 mm.
6. Applied `pcb_apply_manufacturer_rules(manufacturer="jlcpcb_standard")` to project constraints. Profile limits include 0.127 mm track/clearance, 0.3 mm drill/edge clearance, 0.15 mm annular ring. Working zone clearance remains 0.2 mm. Source: https://jlcpcb.com/capabilities/pcb-capabilities/ . Check persisted constraints again after any GUI project save.
7. Removed **123,226 imported top/bottom silk graphics**. These were duplicate/vectorized artwork. Native footprint markings remain; replacement board title, 12 V label, pin labels and final silkscreen cleanup are still needed.
8. Rotated C2 and C4 from 90° to **270°** at the same centers, restoring original pad-number orientation. Both are nonpolarized capacitors. Other original SMT placements were retained.
9. Removed two degenerate tracks, two incorrectly auto-assigned vias and four dangling branch stubs; then added the two correct GND vias, refilled zones and saved the board.

Last saved PCB inspection: **145,394 bytes; 21 footprints; 200 segments; 15 vias; 1 zone; 4 board outline lines; no top-level gr_poly or gr_text.**

The latest `pcb_delete_items` call returned a postcondition-verification warning. Read-only inspection of the saved PCB afterward confirmed that **all eight requested deletion UUIDs are absent**. Do not replay the deletion blindly. Both replacement via additions, zone refill and `pcb_save` reported success.

### Validation status at the stopping point

**The current PCB has NOT been revalidated after the final copper/silkscreen repairs. Do not claim clean DRC or manufacturing readiness.**

The last actual DRC, before that final batch, reported **226 violations + 4 unconnected items; zero courtyard violations**:

- silk overlap 199
- shorting items 6
- solder-mask bridge 6
- dangling track 5
- silk over copper 4
- clearance 2
- dangling via 2
- tracks crossing 1
- silk edge clearance 1

Evidence: `validation/drc_before_final_copper_repairs.json`. Most were duplicate imported silk and swapped C2/C4 pad-number orientation, which the final batch addressed. Remaining counts are **unknown** until a new check runs.

Original schematic image: `fanschematic.png` / `fanschematic-2.png`. Original manufacturing files in `Gerber/` are unchanged.

### Mechanical differences requiring review

- J1 now uses official `Connector:FanPinHeader_1x04_P2.54mm_Vertical`, origin (99.568,159.512), rotation 270°. The original Molex part is `0470531000`. Pad spacing and locating-hole center align, but current library drills/pad shapes differ slightly from original Gerbers: signal drills 1.02 mm vs original about 1.05 mm, locating NPTH 1.1 mm vs original about 1.275 mm. Verify against the actual connector before release.
- J2 uses a standard 1×2 2.54 mm header at (98.806,155.956), rotation 90°; inferred power connector still requires physical selection/review.
- P1 uses a standard 1×3 2.54 mm header at (87.63,172.72), rotation 90°, for an **external** potentiometer. Current header drills are 1.0 mm vs original approximately 1.25 mm. The BOM's Bourns potentiometer is not meant to mount directly in that header footprint.
- H1/H2/H3/H4 centers: (80.01,140.97), (100.584,140.97), (80.01,172.72), (100.584,172.72).

## Selected stock substitutions

| Ref | Selected part | LCSC |
| --- | --- | --- |
| REG1 | ST KF50BD-TR, 5 V / 500 mA / **20 V maximum input** | C222151 |
| C1 | Yageo CC1206JRNPO9BN561, 560 pF, 50 V, NP0, 5%, 1206 | C577166 |
| C4 | Yageo CC1206JRNPOBBN101, 100 pF, 500 V, NP0, 5%, 1206 | C113888 |
| C5 | Panasonic EEEFK1V470AP, 47 µF, 35 V, 6.3 × 5.8 mm | C336786 |

The user confirmed 12 V. **The original “12–28 VDC” silkscreen must not appear on the revised release.** C5 lifetime is 2000 h at 105°C rather than the original part's 5000 h; already disclosed in sourcing notes. Verify regulator capacitor ESR/stability and input bypass requirements against ST's datasheet during final electrical review: https://www.st.com/resource/en/datasheet/kfxx.pdf . No bench test or circuit simulation has been completed.

## Resume procedure

1. Confirm the user wants to resume. Read this file, relevant KiCad skills (`drc-check`, `pcb-design`, `schematic-review`, then `fabrication-output`) and project state. Use dedicated MCP object operations; do not rewrite `.kicad_pcb` / `.kicad_sch` with ad hoc scripts.
2. Re-run **targeted ERC and DRC** on the current saved files. Capture compact summaries; full `run_drc` output is enormous because it repeats every finding as text/evidence/structured payload. Prefer its structured summary and read the generated JSON report for details.
3. Inspect any remaining copper/net issues and verify all pads against the original geometry and reconstructed schematic. Review GND zone connectivity, small remaining stubs, two remaining zero-length tracks, duplicate vias, and DUTY_REF route if flagged. Use MCP cleanup/inspection tools; do not assume the last repair batch passed.
4. Fix remaining native silk/reference placement and add legible **12 V** input polarity, fan pinout, pot header labels and board identification. Preserve pin-1 and C5 positive markings. Render and inspect the board.
5. Verify J1/P1/J2 mechanical parts and hole sizes; confirm connector and external-pot pin mapping. Review regulator decoupling/stability, power budget and fan PWM electrical interface. Clean ERC/DRC alone does not establish functional correctness.
6. Reconcile schematic/PCB parity, DFM and release gates; document any genuine unresolved assumption. Do not silently waive violations or suppress severities.
7. Regenerate Gerbers/drills, SMT BOM, native positions and JLCPCB CPL from the repaired PCB. **Existing CPL/native position exports and BOM workbook have not been updated for C2/C4's final 270° orientations or the new PCB reconstruction.** Update audit/checksums/README/validation evidence and remove stale baseline claims.
8. Upload the new release into JLCPCB, refresh stock/placement preview/pricing, and **save each requested quote in JLCPCB**. The user may need to upload files manually. Final manufacture requires human review; no payment/order was authorized here.
9. Commit meaningful units and push the authorized project branch.

## MCP/browser operational details

The chat MCP tool inventory reported IPC unavailable even with PCB Editor running, because the default API socket belonged to another KiCad app. A fresh full-profile local MCP server successfully reaches PCB Editor using its explicit socket. Last live socket was:

`ipc:///private/tmp/kicad/api-55365.sock`

This is process-specific: rediscover sockets and verify the board on resume. PCB Editor currently has the repaired board open and saved. Avoid saving a stale GUI board over external file edits. The headless edit tools do not all reload the GUI automatically; `pcb_revert` was used only after ensuring all live edits had been saved and the file had been intentionally updated.

Supported local MCP orchestration used `build_server("full")` and `server.call_tool(...)`, with `PYTHONPATH=src`, `KICAD_MCP_PROFILE=full`, `KICAD_MCP_OPERATING_MODE=write`, and `KICAD_API_SOCKET` set to that endpoint. This accesses registered dedicated MCP tools; it does not mutate CAD files directly. Run from the runtime source checkout above, because the venv's editable path otherwise points at a different source tree.

Durable recovery evidence in `KiCad/fancontroller/recovery/`:

- `analyze_original_copper.py`: read-only Gerber connectivity analysis (hardcoded project root).
- `original_copper_connectivity.json`: groups, pin centers, source tracks/vias. **Group IDs are geometry groups, not electrical nets.**
- `call_local_mcp.py`: generic registered-tool orchestration.
- `mcp_restore_copper.json`: historical initial restoration requests.
- `mcp_latest_copper_repairs.json` / `.log`: historical final repair batch and results.

Do not replay historical mutation batches on the current board: they would duplicate tracks/vias or delete items. Original copper groups used: 1=+5V, 5=RAMP, 6=DISCHARGE, 14=COMPARATOR, 45=DUTY_REF, 37=POT_LOW, 48=POT_HIGH, 53=PWM_OUT, 59=+12V, 52=GND. Groups 34/35/36/38/39/40/41/42/43/44/46/47/49/50/51 are also GND based on the functional schematic. Group 21 was the unused balance short and was omitted. Unassigned decorative/floating artwork groups 33 and 56 were omitted.

Read-only analysis environment: `/private/tmp/fan-gerber-analysis` (gerbonara, Shapely, NumPy). Temporary orchestration logs and requests also remain under `/private/tmp/fan-*` but the important artifacts have been copied into the project.

**Tool defect found:** `pcb_set_design_rules` generated a non-native `(rules ...)` `.kicad_dru` file, causing native DRC failure. The new invalid file was moved out of the project to `/private/tmp/fan-invalid-generated-rules.kicad_dru`; no preexisting rules were removed. Used `pcb_apply_manufacturer_rules` instead. Do not invoke the broken custom-rule writer again without fixing/validating it. No MCP source fix was attempted.

Chrome is signed into JLCPCB. Native Chrome upload via extension still fails with “Allow access to file URLs” despite the user enabling it. Do not repeatedly ask for the same permission change. User manually uploaded Gerbers successfully. The saved JLCPCB cart tab was marked as a deliverable and left open. The temporary unsaved quote tab was closed. CUA session handles may not survive; re-read CUA documentation and discover current tabs before operating.

## Stop status

Saved quote request is complete. Schematic ERC was clean before the last mechanical additions. PCB repairs are saved but **final DRC/ERC, release generation, updated upload and engineering approval remain unfinished**. Work is stopped by user request, not because these remaining checks passed.
