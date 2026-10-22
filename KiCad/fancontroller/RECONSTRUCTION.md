# Fan controller KiCad reconstruction

This project was reconstructed from the supplied Gerber, drill, image, and BOM files. It is an editable starting point for design recovery, not a validated replacement for the original CAD source.

## Files

- `fancontroller.kicad_pro`: KiCad 10 project.
- `fancontroller.kicad_pcb`: Gerber artwork imported through KiCad GerbView. It shows the supplied copper, mask, paste, silkscreen, and outline on their corresponding layers.
- `fancontroller.kicad_sch`: recovered component symbols, values, and part identifiers. All 17 installed component references from the populated BOM are present.
- `custom_symbols.kicad_sym` and `sym-lib-table`: project-local TS2938CS50 regulator symbol, using the manufacturer's SOP-8 pin assignment.
- `../../fancontroller_BOM_populated.xlsx`: sourcing workbook with candidates, open matches, and off-board connector options.

## Current limitations

- The schematic symbols are not wired. The supplied schematic images need manual net-by-net transcription and electrical review. ERC currently reports 79 findings, largely unconnected pins and undriven inputs.
- The imported board is artwork without recovered nets or component footprints. The 29 imported vias and 808 tracks do not make it an editable, electrically linked PCB design. Plated and non-plated holes, pad geometry, clearances, and stackup need verification against the original Gerbers and drill files.
- DRC on this artwork import reports 147 findings. This is a check on the reconstructed board file and should not be interpreted as a DRC result for the original CAD design.
- The potentiometer, fan connector, and inferred power connector do not yet have verified KiCad footprints. C5's can diameter, regulator suffix, and connector orientation also need physical confirmation.
- BOM LCSC codes are sourcing leads, not verified JLCPCB assembly selections or live stock commitments. The workbook marks unmatched and out-of-stock lines. J2 is inferred from the board image and requires part selection.

## Before ordering assembly

1. Trace the schematic images and Gerber artwork into a fully wired schematic; verify polarity, pin mapping, and the inferred power connector.
2. Recover or recreate actual pads, footprints, holes, and nets on the board; compare every layer and drill location to the supplied manufacturing files.
3. Resolve BOM candidates and footprints, then rerun ERC and DRC. Export fresh Gerbers, drill files, assembly BOM, and position file from the validated project.

The supplied `Gerber/` directory remains the manufacturing source used for the earlier PCB-only JLCPCB quote, including front and back silkscreen files.
