# ICA V1.a — Scaling Hierarchy (1‑D → 2‑D → 3‑D)

The ICA V1.a architecture is defined across a three‑level scaling hierarchy.
Each level introduces additional structure, dimensionality, and embodiment
while preserving the same operator suite, unified objective, and coherence
constraints. This hierarchy demonstrates that ICA is stable, predictive, and
coherent across increasing cognitive complexity.

---

## 1. Purpose of the Scaling Hierarchy

The scaling hierarchy provides:
- a minimal analytic environment (1‑D)
- a structured spatial environment (2‑D)
- a fully embodied cognitive system (3‑D)

Each level exposes different stability regimes, coherence properties, and
failure modes. Together, they form the canonical evaluation framework for
ICA V1.a.

---

## 2. The 1‑D Analytic Model

The 1‑D model is the simplest environment in which ICA can be analyzed
mathematically and empirically.

### Characteristics
- state: `\( x_t \in \mathbb{R} \)`
- Gaussian noise
- Gaussian belief state
- uncertainty represented as variance
- risk defined as distance from a safe zone
- structural gradients are scalar
- unified objective is fully interpretable

### Why 1‑D Matters
- exposes clarity, uncertainty, and risk interactions
- provides clean stability windows
- allows closed‑form analysis of operator interactions
- demonstrates the necessity of RMO for stability
- reveals Black Swan failure modes

This is the canonical “toy model” for intuition building.

---

## 3. The 2‑D Structured Cognitive Plane

The 2‑D model introduces spatial structure and directional risk.

### Characteristics
- state: `\( x_t \in \mathbb{R}^2 \)`
- spatial uncertainty gradients
- directional risk fields
- multi‑operator interactions become richer
- coherence violations become easier to visualize

### Why 2‑D Matters
- shows how ICA scales beyond toy examples
- reveals cross‑operator interference patterns
- demonstrates long‑horizon stability challenges
- supports visualization of GCC behavior

This is the intermediate model for studying spatial cognition.

---

## 4. The 3‑D Embodied Cognitive System

The 3‑D model introduces embodiment, sensorimotor coupling, and adversarial
perturbations.

### Characteristics
- state: `\( x_t \in \mathbb{R}^3 \)`
- full sensorimotor loop
- environmental coupling
- adversarial disturbances
- long‑horizon stability tracking

### Why 3‑D Matters
- represents deployment‑grade cognitive behavior
- exposes real‑world instability modes
- tests robustness under perturbations
- validates the unified objective under embodiment

This is the highest‑fidelity model in ICA V1.a.

---

## 5. Invariance Across All Three Models

Despite increasing complexity, ICA maintains:
- the same operator suite (UAMC, ASM, TRP, PPO, IGO, RMO, SLO, ICC)
- the same unified objective
- the same coherence constraints (ICC, GCC)
- the same stability conditions
- the same failure modes

This invariance is a core property of ICA V1.a.

---

## 6. Summary

The scaling hierarchy demonstrates:
- ICA’s coherence across dimensionality
- reproducible stability predictions
- consistent failure modes
- robustness of the unified objective
- the necessity of RMO for stability
- the predictive power of GCC

Together, the 1‑D, 2‑D, and 3‑D models form the canonical evaluation suite
for ICA V1.a.

---

End of Scaling Hierarchy Document
