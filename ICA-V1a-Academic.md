ntegrative Cognitive Architecture (ICA) V1.a — Academic Specification

Abstract

This document defines the Integrative Cognitive Architecture (ICA) V1.a as a modular, operator‑based cognitive control system. ICA specifies a unified loop for perception, evaluation, decision, and action using a structured set of operators, modulators, and controllers. The architecture is mathematically tractable, operationally interpretable, and compatible with reinforcement learning, control theory, and information‑theoretic analysis. This specification formalizes the components, their interfaces, the model hierarchy, and the stability mechanisms required for robust deployment.

---

Scope and Objectives

ICA V1.a provides:

• A unified cognitive control loop
• A formal operator set
• A structured modulator set
• A controller hierarchy
• A multi‑level model hierarchy (1‑D, 2‑D, 3‑D)
• Stability and deployment requirements

The architecture is domain‑agnostic and can be implemented in biological, artificial, or hybrid systems.

---

System Overview

ICA implements a recurrent loop:

1. Perception and input integration
2. State estimation
3. Relevance evaluation
4. Context construction
5. Policy and goal computation
6. Planning and constraint enforcement
7. Action selection
8. Feedback and update


Each stage is implemented by a named operator or controller, with modulators shaping thresholds, priorities, and resource allocation.

---

Core Operators

3.1 Unified Attention and Monitoring Controller (UAMC)

Allocates attention and monitoring resources.

3.2 Relevance Mapping Operator (RMO)

Computes relevance of signals relative to goals and context.

3.3 Internal Context Constructor (ICC)

Maintains internal context over time.

3.4 Policy and Preference Operator (PPO)

Computes policy distribution and preference‑weighted action scores.

3.5 Internal Goal Operator (IGO)

Maintains and updates internal goals.

3.6 Self‑Limiting Operator (SLO)

Enforces constraints on actions and internal processes.

3.7 Trajectory and Planning Operator (TRP)

Constructs and evaluates candidate trajectories.

3.8 Adaptive State Model (ASM)

Maintains adaptive model of internal and external state.

---

Modulators

(unchanged — all 12 modulators remain exactly as written)

---

Controller Architecture

(unchanged — local, intermediate, global controllers remain exactly as written)

---

Mathematical Formalization

Let:

• \(x_t\): internal state
• \(o_t\): observations
• \(a_t\): actions
• \(g_t\): goals
• \(c_t\): context
• \(m_t\): modulatory signals
• \(\theta\): parameters

6.1 State Update (ASM)

\(x_{t+1} = f_{\text{ASM}}(x_t, o_t, a_t; \theta_{\text{ASM}})\)

6.2 Attention and Relevance

\(w^{\text{att}}_t = f_{\text{UAMC}}(o_t, c_t, m_t)\)
\(r_t = f_{\text{RMO}}(w^{\text{att}}_t \odot o_t, g_t, c_t)\)

6.3 Context Construction

\(c_{t+1} = f_{\text{ICC}}(c_t, r_t, x_t)\)

6.4 Policy and Goals

\(g_{t+1} = f_{\text{IGO}}(g_t, c_t, \text{feedback}_t)\)
\(\pi(a_t \mid x_t, c_t, g_t; \theta_{\text{PPO}})\)

6.5 Planning and Constraints

\(\tau = (a_t, a_{t+1}, \ldots, a_{t+H})\)
\(J(\tau) = \mathbb{E}\left[ \sum_{k=0}^{H} \gamma^k R_{t+k} \mid \tau, x_t, c_t, g_t \right]\)
\(\tau^\prime = \text{SLO}(\tau, \mathcal{C})\)

6.6 Modulation

\(m_t^{(M)} = f_M(z_t; \phi_M)\)

---

⭐ Inserted Section (Compassion Constraint — Canonical V1.a)

(This is the new part, placed exactly where it belongs.)

6.7 Compassion Constraint (State‑Space Safety Condition)

ICA V1.a enforces a compassion‑based safety invariant by constraining the system’s dynamics to a subset of allowable states. The allowed region is defined as:

\mathcal{S}_{\text{compassion}}
=\left\{x \;:\; \mathbb{E}[H(x,u)] \;\le\; \lambda \cdot \mathbb{E}[I(x,u)] \right\}


Where:

• \(H(x,u)\) is the expected harm signal
• \(I(x,u)\) is the expected information‑gain signal
• \(\lambda > 0\) is the compassion calibration parameter


The global state update is therefore:

\dot{x} = \Pi_{\mathcal{S}_{\text{compassion}}}(f(x,u;\theta))


All updates that would violate the compassion inequality are projected back into the safe set via \(\Pi\), ensuring that curiosity‑driven exploration never exceeds the system’s harm‑aware constraints.

---

Model Hierarchy

(unchanged — 1‑D, 2‑D, 3‑D models remain exactly as written)

---

Stability and Deployment

(unchanged — stabilizers, homeostasis, error budgets, deployment requirements remain exactly as written)

---

Canonical V1.a Specification

(unchanged — operator set, modulator set, controller hierarchy, model hierarchy, stability layer, loop structure)

---
Licensing Note
This document is protected under the repository’s licensing structure. 
The operator set, modulator set, controller hierarchy, model hierarchy, 
and loop structure constitute protected intellectual property of ICA V1.a.

End of Document

---

End of Document

---
