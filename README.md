
# ICA V1.a — Integrative Cognitive Architecture

A unified, mathematically grounded, empirically falsifiable theory of
cognitive stability. This repository contains the complete ICA V1.a
architecture, a framework for predicting system coherence and failure
modes under uncertainty. ICA formalizes cognition as a joint optimization
of controller outputs, making it predictive, mathematically grounded,
and empirically testable.

---

## Recommended Reading Path

### High‑Level Overview
`ICA‑V1a‑Manuscript.md`  
Conceptual and structural explanation of ICA.

### Core Technical Specification
`ICA‑V1a‑Technical‑Specification.md`  
Formal definitions, operators, objective, coherence conditions,
controller dynamics, and stability framing.

### Visual Architecture Map
`ICA‑V1a‑Operator‑Diagram.md`  
Subsystem layout, operator interactions, and coherence pathways.

### Scaling Hierarchy (1‑D → 2‑D → 3‑D)
`ICA‑V1a‑Scaling‑Hierarchy.md`  
Canonical cognitive models and how ICA scales across dimensionality and
embodiment.

### Mathematical Appendix
`ICA‑V1a‑Math‑Appendix.md`  
Formal derivations, gradient structure, stability proofs, and coherence
math.

### Implementation Notes
`ICA‑V1a‑Implementation‑Notes.md`  
Engineering guidance for instantiating ICA in RL and cognitive systems.

### Deployment Notes
`ICA‑V1a‑Deployment‑Notes.md`  
Safe‑mode, escalation, uncertainty handling, and real‑world behavior.

---

## Quick Start (10 Minutes)

- Read the opening sections of `ICA‑V1a‑Manuscript.md`  
- Review `ICA‑V1a‑Operator‑Diagram.md`

This provides a concise understanding of ICA’s structure and purpose.

---

## Controller‑Layer Operators

ICA’s controller suite defines how the system behaves under uncertainty,
risk, and structural change.

| Operator | Purpose                          |
|---------|----------------------------------|
| UAMC    | Signal clarity modulation        |
| ASM     | Uncertainty‑sensitivity          |
| TRP     | Targeted uncertainty reduction   |
| PPO     | Policy‑prior organization        |
| IGO     | Structural gradient integration  |
| RMO     | Risk modulation                  |
| SLO     | Long‑horizon stability           |
| ICC     | Local coherence constraint       |
| GCC     | Global alignment condition       |

These operators jointly determine stability, coherence, and adaptive
behavior.

---

## Unified Objective Function

ICA formalizes cognition as a **single joint optimization** over all
controller outputs, producing a unified, analyzable objective rather
than a collection of heuristics.

The unified objective integrates:
- clarity  
- uncertainty  
- targeted uncertainty reduction  
- priors  
- structural gradients  
- risk  
- long‑horizon stability  
- local coherence (ICC penalty)

This structure makes ICA predictive and mathematically grounded.

---

## Explicit Controller Suite

ICA predicts system behavior under uncertainty, including:
- instability during exploration  
- oscillation or collapse  
- safe‑mode or aggressive‑mode transitions  
- recovery or failure to recover  
- long‑horizon coherence or incoherence  

These predictions are testable across all evaluation models.

---

## Evaluation Models

ICA is evaluated in progressively richer environments.

### 1. 1‑D Toy Model
- continuous state  
- Gaussian noise  
- interpretable dynamics  
- clear stability windows  

### 2. 2‑D Interaction Model
- spatial uncertainty gradients  
- directional risk  
- multi‑operator interactions  

### 3. 3‑D Embodied Model
- sensorimotor coupling  
- adversarial perturbations  
- long‑horizon stability tracking  

Each environment exposes coherence properties and failure modes.

---

## Derived Stability Result

- **RMO is essential for stability.**  
- Systems without RMO exhibit:
  - runaway exploration  
  - adversarial collapse  
  - long‑horizon incoherence  
  - failure to recover from Black Swan events  

This is an empirically falsifiable prediction.

---

## Evidence in This Repository

The repository includes:
- 1‑D toy model demonstrations  
- stability windows and hysteresis analysis  
- Black Swan stress tests  
- controller‑layer predictions  
- mathematical derivations of the coherence condition  
- operator‑interaction analysis across the full controller suite  

---

## Why ICA Matters

ICA provides:
- a scientific theory of cognitive architecture  
- precise, testable claims  
- reproducible stability predictions  
- mathematically defined operator interactions  
- a unified objective for cognitive control  
- a framework for predicting failure modes under uncertainty  

---

## Citation

If referencing ICA V1.a in academic work, cite this repository as the
canonical source.

---

## Licensing

- **Code:** MIT License (`LICENSE`)  
- **Documentation:** CC BY‑ND 4.0 (`LICENSE-DOCS`)  
- See `NOTICE` for a summary of included materials.
