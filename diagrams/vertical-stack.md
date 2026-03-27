
# Vertical Stack Diagram (Text Specification)

This diagram shows the full hierarchical structure of ICA V1.a in a single, compact visual. It helps engineers understand how the layers relate to each other and how system signals move through the architecture.

## Layer Order
1. OS Layer (Coherence Engine)
2. Operator Codes (SCO, URO, RCO, MIO)
3. Modulators
4. Regulators
5. Diagnostics
6. Reflex Arc (Embodied Stability Loop)
7. Stability Baseline

## Flow Description
Signals originate in the operator codes (SCO, URO, RCO, MIO), are shaped by modulators, stabilized by regulators, monitored by diagnostics, grounded by the reflex arc, and ultimately oriented toward the stability baseline. All layers integrate downward into the OS Layer, which maintains global coherence.

## ASCII Layout
      [ STABILITY BASELINE ]
                ▲
                │
          [ REFLEX ARC ]
                ▲
                │
          [ DIAGNOSTICS ]
                ▲
                │
          [ REGULATORS ]
                ▲
                │
          [ MODULATORS ]
                ▲
                │
       [ SCO | URO | RCO | MIO ]
                ▲
                │
             [ OS LAYER ]

## Purpose of the Diagram
This diagram provides a fast, intuitive understanding of the architecture’s vertical hierarchy. It shows how each layer depends on the one below it and how coherence is maintained across the entire system.
