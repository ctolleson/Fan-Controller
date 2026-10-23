# Fan controller KiCad reconstruction

Updated 2026-10-22. This editable KiCad 10 project was recovered from the supplied Gerbers, drill files, BOM and schematic image. The original input files remain unchanged.

## Current validation

**Native KiCad 10.0.6: ERC 0, DRC 0, unconnected 0, courtyard violations 0.** Schematic/PCB parity is 22 references; 63/63 named pad-net assignments match. Existing project/default ignored checks are listed in the raw reports; this repair did not add exclusions or relax severities.

See `release_12v/README.md` for candidate artifacts and complete limitations. The aggregate MCP project gate is still FAIL: mechanical pinless mounting-hole symbols and a rotation-unaware placement heuristic are flagged. An independent transformed-courtyard audit finds all 22 courtyards present and no overlaps. Native checks and this audit do not validate the actual purchased connector mating envelope or functional performance. The working schematic drawing still has text overlaps.

## Recovered design

- Native, netted copper tracks and vias replace the imported Gerber artwork and pseudo-vias. A native B.Cu GND zone provides the return plane.
- Project-local `Recovered2018.pretty` footprints derive from official KiCad 5.0.0 land patterns. See its provenance file. C2/C4 use 270°; C5 is 315°; the regulator native angle is -45° (315°).
- J1 is an official Molex-compatible four-pin fan header; J2 is a generic two-pin 2.54 mm power header; P1 is a generic three-pin header for an external potentiometer. Four 2.2 mm NPTH mounting holes are native mechanical footprints.
- `custom_symbols.kicad_sym` contains the selected KF50BD-TR symbol with proper pin electrical types. Its inhibit pin is grounded, NC is explicit, input is +12 V, output is +5 V.
- LM311 balance pins 5/6 are individually unconnected. Other intentional no-connects are preserved. PWR_FLAGs identify the external supply.
- Native silkscreen includes references, polarity, fan pin labels and **12 V** board identification.
- Added C6, 100 nF / 25 V regulator input bypass (C2167748), following the KF50 datasheet application guidance.

## Sourcing and assembly

The user selected five boards with top-side SMT assembly, stocked substitutions and a 12 V supply. REG1 is KF50BD-TR (20 V maximum input). C1/C4/C5 are the previously approved stocked equivalents. C5 has the previously disclosed 2000 h rather than 5000 h endurance rating at 105°C.

Current candidate assembly is **15 SMT parts per board in 11 BOM rows**. P1/J1/J2 are hand assembled. `release_12v/BOM.csv` and `release_12v/CPL.csv` supersede the root workbook and root draft position file for this revision. The latter are historical sourcing/recovery records and omit C6/final placement corrections.

## Files and evidence

- `fancontroller.kicad_pro`, `.kicad_sch`, `.kicad_pcb`: authoritative editable project.
- `custom_symbols.kicad_sym`, `sym-lib-table`, `Recovered2018.pretty`, `fp-lib-table`: project-local libraries.
- `release_12v/`: candidate Gerber ZIP, drills, 15-part SMT BOM/CPL, plots, source checksums and current validation evidence.
- `recovery/`: historical copper recovery requests and read-only analysis, including the latest repair logs. Do not replay mutation batches.
- `../../JLCPCB_Quote/`: historical original-artwork quotes, including USD 59.91 PCB+14-part assembly before shipping/tax, and USD 42.91 estimated five-board+150 mm stencil+shipping before additional tax. These prices have not been refreshed for the repaired design.
- `../../PASSDOWN.md`: current handoff, exact remaining review steps and runtime details.

No revised vendor upload, bench test, simulation or purchase has occurred. Refresh JLCPCB stock, matched-part placement preview and DFM with the new candidate files, save the quotes, and obtain human engineering review before ordering.
