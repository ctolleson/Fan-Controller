# Fan controller KiCad reconstruction

This project was reconstructed from the supplied Gerber, drill, image, and BOM files. It is an editable starting point for design recovery, not a validated replacement for the original CAD source.

## Files

- `fancontroller.kicad_pro`: KiCad 10 project.
- `fancontroller.kicad_pcb`: Gerber artwork imported through KiCad GerbView, plus 14 surface-mount footprints recovered from the official KiCad 5.0.0 library and aligned with the supplied F.Paste Gerber.
- `fancontroller.kicad_sch`: recovered component symbols, values, and part identifiers. All 17 installed component references from the populated BOM are present.
- `custom_symbols.kicad_sym` and `sym-lib-table`: project-local TS2938CS50 regulator symbol, using the manufacturer's SOP-8 pin assignment.
- `../../fancontroller_BOM_populated.xlsx`: sourcing workbook with candidates, open matches, off-board connector options, and a placement review sheet.
- `Recovered2018.pretty` and `fp-lib-table`: project-local legacy land patterns matching the original artwork. See `Recovered2018.pretty/PROVENANCE.md` for sources and license.
- `../../fancontroller_pick_and_place_DRAFT.csv`: native KiCad position export for the 14 surface-mount parts, explicitly in **millimeters**, with negative Y coordinates. This is not the JLCPCB rotation-corrected CPL.
- `../../JLCPCB_Quote/`: quote-only original Gerber ZIP, SMT BOM, JLCPCB CPL, native position export, placement audit and validation summary.

## Footprint repairs (2026-10-22)

- Replaced modern land patterns with official KiCad 5.0.0 footprints. All 14 parts now match their original paste-pad centers within 0.0005 mm, including the SOIC row spacing and C2/C3 pads.
- Recovered C5 orientation from the asymmetric original silkscreen: native KiCad rotation is 315 degrees, correcting the earlier 135-degree draft. REG1 is also 315 degrees. IC1/IC2/IC3 are 0 degrees. The native orientations match the corresponding legacy footprint silkscreen geometry.
- Fixed the MCP placement/move implementation to rotate absolute pad angles along with footprint orientation. Regression tests pass in the MCP repository, commit `e100c9e`.
- Native courtyard checking now reports zero violations. Total native DRC findings decreased from 667 to 639. No exclusions or waivers were added.

## Current limitations

- The schematic symbols are not wired. The supplied schematic images need manual net-by-net transcription and electrical review. ERC currently reports 79 findings, largely unconnected pins and undriven inputs.
- The imported board has no recovered nets. Its 14 surface-mount footprints sit over Gerber artwork, so the 29 imported vias and 808 tracks are not electrically linked to those pads. Plated and non-plated holes, pad geometry, clearances, and stackup need verification against the original Gerbers and drill files.
- Electrical DRC remains blocked: 639 findings on the artwork reconstruction, including unnetted pad/copper overlaps, imported hole/via artifacts, duplicate silkscreen and default 0.2 mm trace rules applied to original 0.16 mm tracks. These checks cannot certify the original CAD design. See the quote validation summary for exact counts.
- The JLCPCB CPL applies the MCP SOIC rotation correction (IC1/IC2/IC3: 270 degrees; REG1: 225 degrees). Coordinates remain in the original Gerber frame. Verify all component centers, pin 1 and C5 polarity in JLCPCB's matched-part preview before an order.
- P1, J1, and the inferred J2 have drill-hole locations but no placed footprints. Their mechanical parts need confirmation. C5's can diameter, regulator suffix, and connector orientation also need physical confirmation.
- BOM LCSC codes are sourcing leads, not verified JLCPCB assembly selections or live stock commitments. The workbook marks unmatched and out-of-stock lines. J2 is inferred from the board image and requires part selection.

## Before ordering assembly

1. Trace the schematic images and Gerber artwork into a fully wired schematic; verify polarity, pin mapping, and the inferred power connector.
2. Recover or recreate actual pads, holes, copper and nets on the board; compare every layer and drill location to the supplied manufacturing files. Resolve the three unplaced through-hole parts if they will be included in a later assembly scope.
3. Resolve BOM candidates and footprints, then rerun ERC and DRC. Export fresh Gerbers, drill files, assembly BOM, and position file from the validated project.

The current quote scope is five boards with 14 SMT parts per board. P1, J1 and J2 are excluded for hand assembly. The supplied `Gerber/` directory remains the source of the quote ZIP, including front and back silkscreen files. No replacement fabrication Gerbers were exported from the incomplete reconstruction. A quote does not approve fabrication or resolve the remaining electrical checks.
