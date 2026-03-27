
Integrative Cognitive Architecture (ICA) — V1.a Manuscript
A Unified, Predictive, and Mathematically Grounded Framework for Cognitive Stability

© 2026 Sean Meehan. All rights reserved.

LICENSE NOTICE (ALWAYS VISIBLE IN THIS FILE)
This manuscript is licensed under the Creative Commons Attribution–NoDerivatives 4.0 International License (CC BY‑ND 4.0).
All code in this repository is licensed under the MIT License.
See LICENSE, LICENSE-DOCS, COPYRIGHT, and NOTICE in the repository root for full terms.
END LICENSE NOTICE

Table of Contents
Abstract
Introduction
Core Hypothesis
Architectural Overview
Controller‑Layer Operators
Unified Objective Function
Integrative Coherence Condition (ICC)
Stability Theory
Failure Modes
Evaluation Models
Empirical Evidence
Why ICA Matters
Conclusion
Licensing Note

Abstract
Integrative Cognitive Architecture (ICA) proposes that cognitive stability arises from the coordinated interaction of a structured suite of controller‑layer operators. ICA provides a mathematically grounded, empirically testable framework that predicts both stable behavior and failure modes under uncertainty. The architecture is defined by a unified objective function, the Integrative Coherence Condition (ICC), and a set of operators that regulate clarity, uncertainty, risk, structural gradients, and long‑horizon stability. ICA is falsifiable, reproducible, and evaluated across 1‑D, 2‑D, and 3‑D environments.

Introduction
Cognitive systems—biological or artificial—must maintain stability while operating under uncertainty. Traditional approaches often rely on heuristic combinations of objectives, leading to unpredictable behavior, instability, or collapse under adversarial or high‑uncertainty conditions. ICA addresses this gap by introducing a unified, mathematically defined controller suite that predicts when a system will remain stable, when it will fail, and why.

Core Hypothesis
ICA’s central hypothesis is that cognitive stability emerges only when controller‑layer operators are jointly optimized under the Integrative Coherence Condition (ICC). These operators regulate signal clarity, uncertainty sensitivity, targeted uncertainty reduction, policy‑prior structure, structural gradient integration, risk modulation, and long‑horizon stability. A key derived result is that RMO (Risk‑Modulation Operator) is a required stabilizer. Systems lacking RMO exhibit runaway exploration, adversarial collapse, and long‑horizon incoherence.

Architectural Overview
ICA consists of three interacting components:
1. Controller‑Layer Operators
2. Unified Objective Function
3. Integrative Coherence Condition (ICC)
These components define a closed‑loop system that selects actions, updates internal state, and maintains stability across time.

Figure placeholder: Figure 1: ICA Operator Flow — figures/operator_flow.png

Controller‑Layer Operators
The operator suite includes:
UAMC — signal clarity modulation
ASM — uncertainty sensitivity
TRP — targeted uncertainty reduction
PPO — policy‑prior organization
IGO — structural gradient integration
RMO — risk modulation
SLO — long‑horizon stability
ICC — coherence constraint operator

Operator Definitions (Plain Text)
UAMC(x_t) = negative norm of gradient of belief b_t
ASM(σ_t) = α times σ_t
TRP(a_t) = negative expected uncertainty at next step given action a_t
PPO(a_t) = log of prior policy π₀(a_t | x_t)
IGO(g_t) = negative norm of change in structural gradient
RMO(r_t) = negative β times risk r_t
SLO(x_{t:t+k}) = negative sum of distances between future states and current state

Unified Objective Function
J = sum of λ_i times operator outputs minus λ₈ times ICC
Action selection: a_t = action that maximizes J(x_t, a)

Integrative Coherence Condition (ICC)
ICC = norm of the sum of gradients of all operators, with SLO subtracted
Coherence condition: ICC must be less than or equal to ε
Discrepancy signal: D_t = norm of ICC at time t

The discrepancy signal predicts stability, instability, oscillation, collapse, and recovery difficulty.

Stability Theory
ICA defines stability through four conditions:
1. Bounded divergence: change in state less than δ
2. Coherence maintained: ICC ≤ ε
3. Risk bounded: r_t < r_max
4. Uncertainty controlled: σ_{t+1} ≤ σ_t + γ
When these conditions hold, the system remains stable across time.

Failure Modes
Runaway exploration — caused by insufficient ASM/TRP
Adversarial collapse — caused by RMO failure
Long‑horizon incoherence — caused by SLO violation
Black Swan non‑recovery — caused by ICC remaining high

Evaluation Models
1‑D Toy Model: continuous state, Gaussian noise, Gaussian belief, uncertainty equals variance, risk equals distance from safe zone. Figure placeholder: [Insert 1‑D model diagram here]

2‑D Interaction Model: spatial uncertainty gradients, directional risk, multi‑axis perturbations. Figure placeholder: [Insert 2‑D model diagram here]

3‑D Embodied Model: sensorimotor coupling, adversarial perturbations, long‑horizon stability tracking. Figure placeholder: [Insert 3‑D model diagram here]

Empirical Evidence
ICA includes stability windows, hysteresis analysis, Black Swan stress tests, operator‑interaction studies, and coherence‑violation predictions. These results demonstrate that ICA’s predictions are reproducible and falsifiable.

Why ICA Matters
ICA reframes cognitive architecture as a scientific theory. It provides mathematical structure, predictive power, falsifiable claims, reproducible evaluations, and interpretable operator interactions. This positions ICA as a rigorous foundation for future cognitive systems.

Conclusion
ICA V1.a defines a unified, predictive, and mathematically grounded framework for cognitive stability. Its operator suite, coherence condition, and unified objective form a complete architecture capable of predicting both stable behavior and failure modes.

Licensing Note
This manuscript is protected under the Creative Commons Attribution–NoDerivatives 4.0 International License (CC BY‑ND 4.0). All code in this repository is licensed under the MIT License. See LICENSE, LICENSE-DOCS, COPYRIGHT, and NOTICE for full terms.
