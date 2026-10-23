# JLCPCB quote draft

Scope: **5 boards, top-side SMT assembly, 14 components per board**, green solder mask and white silkscreen. P1, J1 and J2 are excluded for hand assembly.

## Obtained quote: USD 59.91 before shipping and tax

JLCPCB calculated this quote on 2026-10-22 for all 11 BOM lines / 14 SMT parts per board. The draft is automatically saved at [JLCPCB PCBA Viewer](https://cart.jlcpcb.com/smt-order/?pcbFileNo=30188cbaad6147518de35d540fbe1b3e). No order was placed.

| Charge | USD |
| --- | ---: |
| Five bare PCBs | 4.00 |
| PCBA setup | 8.24 |
| Stencil | 1.55 |
| Components, including attrition | 13.64 |
| Extended component fees | 30.90 |
| SMT assembly | 0.67 |
| Nitrogen reflow | 0.91 |
| **Total before shipping and tax** | **59.91** |

Displayed build times: PCB 24 hours; assembly 1–2 days. Shipping/tax were not finalized. See `quote_summary.json` and `quote_59_91.png` for evidence.

The user authorized stocked replacements and confirmed a **12 V supply**. REG1 is KF50BD-TR (C222151), C1 is CC1206JRNPO9BN561 (C577166), C4 is CC1206JRNPOBBN101 (C113888), and C5 is EEEFK1V470AP (C336786). The regulator input limit is 20 V, so the unchanged original **12–28 V silkscreen is not valid for this build**. C5 has the same 6.3 × 5.8 mm case and a higher voltage rating, but its endurance rating is 2,000 hours at 105 °C versus the original 5,000 hours. Details and primary sources are in `substitutions.json`.

## Upload files

- `fancontroller_original_gerbers.zip`: unchanged supplied Gerbers and drill files, including front/back silkscreen. This does not contain exports from the reconstructed PCB.
- `BOM.csv`: current quote selections, 11 lines covering 14 SMT references, with all LCSC codes populated. Uses ASCII comments for JLCPCB CSV compatibility.
- `BOM_uploaded_initial.csv`: the initial uploaded original-part BOM, before replacements were selected in JLCPCB.
- `CPL.csv`: JLCPCB columns, millimeters, original Gerber coordinate frame, Top layer. IC1/IC2/IC3 are corrected to 270 degrees and REG1 to 225 degrees using the MCP JLCPCB SOIC rule. C5 is 315 degrees following recovery from original silkscreen. The vendor preview was visually checked for centers, IC pin-1 markers and C5 polarity; final vendor DFM review is still required.

## Evidence

- `positions-kicad-mm.csv`: native KiCad millimeter position export before JLCPCB rotation correction.
- `placement_audit.json`: all 14 footprints match original paste pad centers within 0.0005 mm.
- `validation_summary.json`: exact DRC counts and remaining gates.
- `source_manifest.json`: source and upload checksums.

## Open blockers

The reconstructed schematic is unwired (ERC 79). The imported artwork lacks nets (DRC 639), although courtyard checking now passes. No waivers or exclusions were added. This folder is a **quote draft**, not an approved manufacturing release. Resolve electrical reconstruction and vendor part/placement review before ordering.

The original C1, C4, C5 and REG1 parts had no available assembly stock. Stocked alternatives were matched in the live quote, and all 11 lines were confirmed. The editable KiCad reconstruction retains the recovered original component values; the workbook and quote BOM record the proposed 12 V build selections. Verify the replacements electrically before releasing a revised design.
