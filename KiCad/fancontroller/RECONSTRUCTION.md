# Fan controller KiCad reconstruction

This project was reconstructed from the supplied Gerber, drill, image, and BOM files. It is an editable starting point for design recovery, not a validated replacement for the original CAD source.

## Files

- `fancontroller.kicad_pro`: KiCad 10 project.
- `fancontroller.kicad_pcb`: Gerber artwork imported through KiCad GerbView, plus 14 draft surface-mount footprints placed at component centers recovered from the supplied F.Paste Gerber.
- `fancontroller.kicad_sch`: recovered component symbols, values, and part identifiers. All 17 installed component references from the populated BOM are present.
- `custom_symbols.kicad_sym` and `sym-lib-table`: project-local TS2938CS50 regulator symbol, using the manufacturer's SOP-8 pin assignment.
- `../../fancontroller_BOM_populated.xlsx`: sourcing workbook with candidates, open matches, off-board connector options, and a placement review sheet.
- `../../fancontroller_pick_and_place_DRAFT.csv`: unvalidated KiCad position export for the 14 placed surface-mount parts. KiCad's default export uses inches and negative Y coordinates. Do not submit this file for assembly yet.

## Current limitations

- The schematic symbols are not wired. The supplied schematic images need manual net-by-net transcription and electrical review. ERC currently reports 79 findings, largely unconnected pins and undriven inputs.
- The imported board has no recovered nets. Its 14 surface-mount footprints sit over Gerber artwork, so the 29 imported vias and 808 tracks are not electrically linked to those pads. Plated and non-plated holes, pad geometry, clearances, and stackup need verification against the original Gerbers and drill files.
- The placement review sheet records measured pad-center differences between the selected KiCad library footprints and the supplied paste Gerber. The four SOIC footprints differ by about 0.225 mm across the rows; C2/C3 differ by 0.1 mm. C5 polarity and REG1 pin orientation still need confirmation.
- The placement quality gate fails for C2/IC2, C3/IC3, and C5/REG1 courtyard overlaps. DRC on the reconstructed board reports 667 findings after footprint placement. These are checks on this artwork import, not on the original CAD design.
- P1, J1, and the inferred J2 have drill-hole locations but no placed footprints. Their mechanical parts need confirmation. C5's can diameter, regulator suffix, and connector orientation also need physical confirmation.
- BOM LCSC codes are sourcing leads, not verified JLCPCB assembly selections or live stock commitments. The workbook marks unmatched and out-of-stock lines. J2 is inferred from the board image and requires part selection.

## Before ordering assembly

1. Trace the schematic images and Gerber artwork into a fully wired schematic; verify polarity, pin mapping, and the inferred power connector.
2. Recover or recreate actual pads, footprints, holes, and nets on the board; compare every layer and drill location to the supplied manufacturing files. Resolve the three unplaced through-hole parts and the courtyard/pad-offset findings.
3. Resolve BOM candidates and footprints, then rerun ERC and DRC. Export fresh Gerbers, drill files, assembly BOM, and position file from the validated project.

The supplied `Gerber/` directory remains the manufacturing source used for the earlier PCB-only JLCPCB quote, including front and back silkscreen files.
