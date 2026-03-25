Integrative Cognitive Architecture (ICA) V1.a — Academic Specification

Abstract

This document defines the Integrative Cognitive Architecture (ICA) V1.a as a modular, operator‑based cognitive control system. ICA specifies a unified loop for perception, evaluation, decision, and action using a structured set of operators, modulators, and controllers. The architecture is mathematically tractable, operationally interpretable, and compatible with reinforcement learning, control theory, and information‑theoretic analysis. This specification formalizes the components, their interfaces, the model hierarchy, and the stability mechanisms required for robust deployment.

---

1. Scope and Objectives

ICA V1.a provides:

• A unified cognitive control loop
• A formal operator set
• A structured modulator set
• A controller hierarchy
• A multi‑level model hierarchy (1‑D, 2‑D, 3‑D)
• Stability and deployment requirements


The architecture is domain‑agnostic and can be implemented in biological, artificial, or hybrid systems.

---

2. System Overview

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

3. Core Operators

3.1 Unified Attention and Monitoring Controller (UAMC)

Role: Allocates attention and monitoring resources.
Inputs: Sensory features, task demands, modulators.
Outputs: Attention weights, monitoring priorities, gating signals.
Function: Computes weighted routing of signals to downstream operators.

---

3.2 Relevance Mapping Operator (RMO)

Role: Computes relevance of signals relative to goals and context.
Inputs: Attended signals, goals, context.
Outputs: Relevance scores, ranked signals.
Function: Maps features into a relevance space for decision‑making.

---

3.3 Internal Context Constructor (ICC)

Role: Maintains internal context over time.
Inputs: Relevance‑filtered signals, historical state, predictions.
Outputs: Context state vector.
Function: Integrates information across time to maintain contextual continuity.

---

3.4 Policy and Preference Operator (PPO)

Role: Computes policy distribution and preference‑weighted action scores.
Inputs: Context, value estimates, modulators.
Outputs: Policy distribution.
Function: Combines learned policies with current preferences.

---

3.5 Internal Goal Operator (IGO)

Role: Maintains and updates internal goals.
Inputs: Context, feedback, long‑term objectives.
Outputs: Active goal set, goal priorities.
Function: Selects and updates goals based on feedback and constraints.

---

3.6 Self‑Limiting Operator (SLO)

Role: Enforces constraints on actions and internal processes.
Inputs: Proposed actions, constraints, risk estimates.
Outputs: Allowed action set, suppression signals.
Function: Ensures behavior remains within acceptable bounds.

---

3.7 Trajectory and Planning Operator (TRP)

Role: Constructs and evaluates candidate trajectories.
Inputs: Goals, policies, predictions, constraints.
Outputs: Candidate trajectories, selected plan.
Function: Performs multi‑step planning under uncertainty.

---

3.8 Adaptive State Model (ASM)

Role: Maintains adaptive model of internal and external state.
Inputs: Observations, actions, prediction errors.
Outputs: State estimates, updated parameters.
Function: Provides state representation for prediction and control.

---

4. Modulators

Modulators adjust thresholds, priorities, and resource allocation.

4.1 Salience Filter Modulator (SFM)

Weights signals by salience.

4.2 Stability and Anchoring Modulator (SAM)

Stabilizes representations against noise and drift.

4.3 Drift Regulation Modulator (DRM)

Compensates for slow drift in parameters.

4.4 Workload and Effort Modulator (WEM)

Adjusts resource allocation based on workload.

4.5 Homeostatic Regulation Modulator (HRM)

Maintains global homeostatic balance.

4.6 Priority Balancing Modulator (PBM)

Balances competing priorities.

4.7 Policy Gating Modulator (PGM)

Gates which policies are active.

4.8 Error Budget Modulator (EBM)

Allocates allowable error across components.

4.9 Memory Encoding Modulator (MEM)

Determines which experiences are encoded.

4.10 Integration Bandwidth Modulator (IBM)

Controls temporal integration bandwidth.

4.11 Timing Modulator (TM)

Modulates timing of operations and cycles.

4.12 Mindfulness Modulator (MM)

Modulates meta‑monitoring and introspective evaluation.

---

5. Controller Architecture

5.1 Local Controllers

Short‑timescale, subsystem‑specific control using:
UAMC, RMO, ICC, SFM, SAM, WEM.

5.2 Intermediate Controllers

Cross‑subsystem coordination using:
PPO, IGO, TRP, PBM, PGM, EBM, MEM.

5.3 Global Controller

Long‑timescale coherence using:
HRM, DRM, IBM, TM, MM, ASM, SLO.

---

6. Mathematical Formalization

Let:

• \( x_t \): internal state
• \( o_t \): observations
• \( a_t \): actions
• \( g_t \): goals
• \( c_t \): context
• \( m_t \): modulatory signals
• \( \theta \): parameters


6.1 State Update (ASM)

x_{t+1} = f_{\text{ASM}}(x_t, o_t, a_t; \theta_{\text{ASM}})


6.2 Attention and Relevance

w^{\text{att}}_t = f_{\text{UAMC}}(o_t, c_t, m_t)


r_t = f_{\text{RMO}}(w^{\text{att}}_t \odot o_t, g_t, c_t)


6.3 Context Construction

c_{t+1} = f_{\text{ICC}}(c_t, r_t, x_t)


6.4 Policy and Goals

g_{t+1} = f_{\text{IGO}}(g_t, c_t, \text{feedback}_t)


\pi(a_t \mid x_t, c_t, g_t; \theta_{\text{PPO}})


6.5 Planning and Constraints

\tau = (a_t, a_{t+1}, \ldots, a_{t+H})


J(\tau) = \mathbb{E}\left[ \sum_{k=0}^{H} \gamma^k R_{t+k} \mid \tau, x_t, c_t, g_t \right]


\tau^\prime = \text{SLO}(\tau, \mathcal{C})


6.6 Modulation

m_t^{(M)} = f_M(z_t; \phi_M)


---

7. Model Hierarchy

7.1 1‑D Model

Scalar or low‑dimensional state variables.
Used for minimal implementations and analytical stability.

7.2 2‑D Model

Structured state spaces (vectors, grids).
Supports multi‑dimensional control and planning.

7.3 3‑D Model

High‑dimensional, multi‑modal state spaces.
Full operator and modulator deployment.

---

8. Stability and Deployment

8.1 Stabilizer Parameters

Bounds on:

• Feedback gains
• Integration windows
• Learning rates
• Modulation strength


8.2 Homeostatic and Drift Control

HRM + DRM maintain long‑term stability.

8.3 Error Budgets

EBM distributes allowable error across components.

8.4 Deployment Requirements

• Mapping from observations to UAMC/RMO/ASM
• Mapping from actions to environment
• Initialization of stabilizers
• Monitoring of stability indicators


---

9. Canonical V1.a Specification

Canonical elements:

1. Operator set:
UAMC, RMO, ICC, PPO, IGO, SLO, TRP, ASM
2. Modulator set:
SFM, SAM, DRM, WEM, HRM, PBM, PGM, EBM, MEM, IBM, TM, MM
3. Controller hierarchy
4. Model hierarchy
5. Stability layer
6. Recurrent loop structure


Any implementation preserving these roles and interactions qualifies as ICA V1.a.

---

10. Licensing Note

This document is protected under the repository’s licensing structure.
The operator set, modulator set, controller hierarchy, model hierarchy, and loop structure constitute protected intellectual property of ICA V1.a.

---

End of Document

---
