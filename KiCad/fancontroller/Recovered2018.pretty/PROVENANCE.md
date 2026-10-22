# Recovered land patterns

Source: official [KiCad footprint library, tag 5.0.0](https://github.com/KiCad/kicad-footprints/tree/5.0.0), retrieved 2026-10-22.

Original library paths:

- `Capacitor_SMD.pretty/CP_Elec_6.3x5.8.kicad_mod`
- `Capacitor_SMD.pretty/C_0603_1608Metric_Pad1.05x0.95mm_HandSolder.kicad_mod`
- `Capacitor_SMD.pretty/C_1206_3216Metric_Pad1.42x1.75mm_HandSolder.kicad_mod`
- `Resistor_SMD.pretty/R_1206_3216Metric_Pad1.42x1.75mm_HandSolder.kicad_mod`
- `Package_SO.pretty/SOIC-8_3.9x4.9mm_P1.27mm.kicad_mod`

Converted to current syntax using official KiCad 10 `kicad-cli fp upgrade --force`. Land patterns were selected by matching original paste pads and asymmetric silkscreen strokes. Board placement and rotation were performed through KiCad MCP tools.

The included `LICENSE.md` is the license shipped with the source tag (CC BY-SA 4.0 with KiCad library exception). This provenance file records the conversion; original authorship remains with the KiCad library contributors.
