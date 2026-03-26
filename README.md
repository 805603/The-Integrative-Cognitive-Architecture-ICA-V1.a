Integrative Cognitive Architecture (ICA) V1.a — Academic Specification

Abstract

This document specifies the Integrative Cognitive Architecture (ICA) V1.a as a formal, modular, and implementable cognitive control system. ICA defines a set of operators, modulators, and controllers that together implement a unified loop for perception, evaluation, decision, and action. The architecture is designed to be mathematically tractable, operationally interpretable, and compatible with reinforcement learning (RL), control theory, and information‑theoretic analysis. This specification describes the components, their interfaces, the model hierarchy, and stability considerations for deployment.

---

1. Scope and objectives

ICA V1.a defines:

• A core control loop for cognitive processing.
• A set of operators that transform internal and external signals.
• A set of modulators that shape priorities, thresholds, and resource allocation.
• A controller hierarchy that coordinates behavior across timescales.
• A model hierarchy (1‑D, 2‑D, 3‑D) for increasing representational richness.
• A stability and deployment layer for robust operation under uncertainty.


The architecture is domain‑agnostic: it can be instantiated in biological, artificial, or hybrid systems, provided the required signals and state variables are available.

---

2. System overview

At the highest level, ICA implements a recurrent loop:

1. Perception and input integration
2. State estimation and internal representation
3. Evaluation and prioritization
4. Policy selection and control
5. Action and output
6. Feedback and update


This loop is implemented through a set of named operators and modulators. Each operator has:

• Defined inputs
• Defined outputs
• A role in the control loop
• A location in the model hierarchy


The architecture is designed so that:

• Each operator is locally interpretable.
• The global behavior emerges from compositional interactions.
• Stability can be analyzed using standard tools from control theory.


---

3. Core operators

This section defines the primary operators used in ICA V1.a. Names are given in their canonical technical form.

3.1 Unified Attention and Monitoring Controller (UAMC)

Role:
UAMC manages allocation of attention and monitoring resources over internal and external signals.

Inputs:

• Sensory features and latent states
• Task demands and goals
• Modulatory signals (e.g., from PBM, HRM)


Outputs:

• Attention weights over inputs
• Monitoring priorities
• Gating signals for downstream operators


Function:
UAMC computes a weighting over candidate signals and routes them to downstream operators according to current priorities and constraints.

---

3.2 Relevance Mapping Operator (RMO)

Role:
RMO evaluates the relevance of signals with respect to current goals and context.

Inputs:

• Attended signals from UAMC
• Goal representations
• Contextual state


Outputs:

• Relevance scores
• Filtered or ranked signal set


Function:
RMO maps raw or latent features into a relevance space, enabling the system to focus on information that is likely to influence decisions.

---

3.3 Internal Context Constructor (ICC)

Role:
ICC builds and maintains an internal representation of context over time.

Inputs:

• Relevance‑filtered signals from RMO
• Historical state
• Model predictions


Outputs:

• Context state vector
• Contextual features for other operators


Function:
ICC integrates information across time to maintain a working context that conditions evaluation, prediction, and control.

---

3.4 Policy and Preference Operator (PPO)

Role:
PPO encodes policies and preferences over possible actions or trajectories.

Inputs:

• Context state from ICC
• Value estimates
• Modulatory signals (e.g., PBM, PGM)


Outputs:

• Policy distribution over actions
• Preference‑weighted action scores


Function:
PPO combines learned policies with current preferences to produce a control‑ready action distribution.

---

3.5 Internal Goal Operator (IGO)

Role:
IGO maintains and updates internal goals.

Inputs:

• Context state
• Feedback signals
• Long‑term objectives


Outputs:

• Active goal set
• Goal priorities


Function:
IGO selects and updates goals based on feedback, constraints, and higher‑level objectives.

---

3.6 Self‑Limiting Operator (SLO)

Role:
SLO enforces constraints on behavior and internal processes.

Inputs:

• Proposed actions or plans
• Constraint set
• Risk and cost estimates


Outputs:

• Allowed action set
• Suppression or modification signals


Function:
SLO ensures that actions and internal processes remain within acceptable bounds (safety, ethics, resource limits, etc.).

---

3.7 Trajectory and Planning Operator (TRP)

Role:
TRP constructs and evaluates candidate trajectories over time.

Inputs:

• Goals from IGO
• Policies from PPO
• Model predictions
• Constraints from SLO


Outputs:

• Candidate trajectories
• Selected plan or sequence


Function:
TRP performs planning over multiple steps, evaluating trajectories under uncertainty and constraints.

---

3.8 Adaptive State Model (ASM)

Role:
ASM maintains an adaptive model of the system’s internal and external state.

Inputs:

• Observations
• Actions
• Prediction errors


Outputs:

• State estimates
• Updated model parameters


Function:
ASM provides a state representation that supports prediction, control, and evaluation.

---

4. Modulators

Modulators shape how operators behave without replacing their core logic. They adjust thresholds, priorities, and resource allocation.

4.1 Salience Filter Modulator (SFM)

Role:
SFM modulates which signals are treated as salient.

Inputs:

• Raw or preprocessed signals
• Context state
• Learned salience parameters


Outputs:

• Salience‑weighted signals
• Salience scores


---

4.2 Stability and Anchoring Modulator (SAM)

Role:
SAM stabilizes internal representations and anchors them against noise and drift.

Inputs:

• State estimates
• Prediction errors
• Stability parameters


Outputs:

• Adjusted state representations
• Stabilizing feedback signals


---

4.3 Drift Regulation Modulator (DRM)

Role:
DRM regulates slow drift in parameters and internal states.

Inputs:

• Long‑term statistics
• Parameter trajectories
• Performance metrics


Outputs:

• Parameter corrections
• Drift compensation signals


---

4.4 Workload and Effort Modulator (WEM)

Role:
WEM modulates resource allocation based on workload and effort.

Inputs:

• Task demands
• Performance metrics
• Resource usage


Outputs:

• Resource allocation signals
• Effort scaling parameters


---

4.5 Homeostatic Regulation Modulator (HRM)

Role:
HRM maintains homeostatic balance across the system.

Inputs:

• Global state indicators
• Stress or overload signals
• Long‑term constraints


Outputs:

• Global modulation signals
• Adjustments to thresholds and gains


---

4.6 Priority Balancing Modulator (PBM)

Role:
PBM balances competing priorities (e.g., short‑term vs long‑term).

Inputs:

• Goal set from IGO
• Context state
• Performance metrics


Outputs:

• Priority weights
• Adjusted goal ordering


---

4.7 Policy Gating Modulator (PGM)

Role:
PGM gates which policies are available or emphasized.

Inputs:

• Policy library
• Context state
• Constraints


Outputs:

• Gated policy set
• Policy activation weights


---

4.8 Error Budget Modulator (EBM)

Role:
EBM allocates allowable error across components.

Inputs:

• Performance targets
• Risk tolerance
• Model uncertainty


Outputs:

• Error budgets for operators
• Tuning parameters for controllers


---

4.9 Memory Encoding Modulator (MEM)

Role:
MEM modulates which experiences are encoded into memory.

Inputs:

• Salience scores
• Prediction errors
• Goal relevance


Outputs:

• Encoding decisions
• Memory update signals


---

4.10 Integration Bandwidth Modulator (IBM)

Role:
IBM controls the effective bandwidth of integration over time.

Inputs:

• Temporal statistics
• Task demands
• Stability constraints


Outputs:

• Integration window parameters
• Temporal smoothing factors


---

4.11 Timing Modulator (TM)

Role:
TM modulates timing of operations and control cycles.

Inputs:

• Temporal constraints
• External timing cues
• Internal state


Outputs:

• Cycle timing parameters
• Scheduling adjustments


---

4.12 Mindfulness Modulator (MM)

Role:
MM modulates the degree of meta‑monitoring and introspective evaluation.

Inputs:

• Monitoring signals
• Performance metrics
• Stability indicators


Outputs:

• Meta‑monitoring gain
• Introspection‑related control signals


---

5. Controller architecture

ICA V1.a organizes operators and modulators into a controller hierarchy.

5.1 Local controllers

Local controllers operate on short timescales and specific subsystems (e.g., perception, motor control, local evaluation). They use:

• UAMC, RMO, ICC for local selection and context
• SFM, SAM, WEM for local modulation


5.2 Intermediate controllers

Intermediate controllers coordinate across subsystems and timescales:

• PPO, IGO, TRP for policy, goals, and planning
• PBM, PGM, EBM, MEM for shaping intermediate behavior


5.3 Global controller

The global controller maintains overall stability and long‑term coherence:

• HRM, DRM, IBM, TM, MM for global modulation
• ASM for global state estimation
• SLO for global constraint enforcement


---

6. Mathematical formalization

This section sketches the mathematical structure of ICA V1.a. Let:

• \( x_t \) be the internal state at time \( t \)
• \( o_t \) be observations
• \( a_t \) be actions
• \( g_t \) be goals
• \( c_t \) be context
• \( m_t \) be modulatory signals
• \( \theta \) be parameters of models and policies


6.1 State update

The Adaptive State Model (ASM) defines:

x_{t+1} = f_{\text{ASM}}(x_t, o_t, a_t; \theta_{\text{ASM}})


where \( f_{\text{ASM}} \) is an adaptive function (e.g., recurrent network, state‑space model).

6.2 Attention and relevance

UAMC computes attention weights:

w^{\text{att}}_t = f_{\text{UAMC}}(o_t, c_t, m_t)


RMO computes relevance scores:

r_t = f_{\text{RMO}}(w^{\text{att}}_t \odot o_t, g_t, c_t)


where \( \odot \) denotes elementwise multiplication.

6.3 Context construction

ICC updates context:

c_{t+1} = f_{\text{ICC}}(c_t, r_t, x_t)


6.4 Policy and goals

IGO updates goals:

g_{t+1} = f_{\text{IGO}}(g_t, c_t, \text{feedback}_t)


PPO computes a policy:

\pi(a_t \mid x_t, c_t, g_t; \theta_{\text{PPO}})


6.5 Planning and constraints

TRP constructs trajectories:

\tau = (a_t, a_{t+1}, \ldots, a_{t+H})


and evaluates them via:

J(\tau) = \mathbb{E}\left[ \sum_{k=0}^{H} \gamma^k R_{t+k} \mid \tau, x_t, c_t, g_t \right]


SLO enforces constraints:

\tau^\prime = \text{SLO}(\tau, \mathcal{C})


where \( \mathcal{C} \) is the constraint set.

6.6 Modulation

Each modulator \( M \) can be represented as:

m_t^{(M)} = f_M(z_t; \phi_M)


where \( z_t \) is the relevant input set (e.g., state, performance metrics, goals), and \( \phi_M \) are modulator parameters. These signals adjust gains, thresholds, and weights in the operators and controllers.

---

7. Model hierarchy

ICA V1.a supports a hierarchy of models with increasing representational richness.

7.1 1‑D model

The 1‑D model uses scalar or low‑dimensional state variables and simple controllers. It is suitable for:

• Minimal implementations
• Didactic examples
• Analytical stability analysis


7.2 2‑D model

The 2‑D model introduces structured state spaces (e.g., vectors, grids) and richer interactions between operators. It supports:

• Multi‑dimensional control
• Basic planning
• Non‑trivial modulation


7.3 3‑D model

The 3‑D model supports high‑dimensional, multi‑modal state spaces and full operator/modulator deployment. It is intended for:

• Complex cognitive tasks
• Multi‑objective control
• Rich planning and adaptation


The same operator and modulator definitions apply across all three levels; only the dimensionality and complexity of the underlying models change.

---

8. Stability and deployment

8.1 Stabilizer parameters

ICA V1.a includes explicit stabilizer parameters that bound:

• Gain on feedback loops
• Integration windows
• Learning rates
• Modulation strength


These parameters are tuned to ensure that closed‑loop behavior remains within acceptable bounds.

8.2 Homeostatic and drift control

HRM and DRM jointly maintain long‑term stability by:

• Monitoring global indicators (e.g., error, variance, resource usage)
• Adjusting thresholds and gains
• Compensating for slow drift in parameters


8.3 Error budgets

EBM allocates error budgets across components, ensuring that no single operator or controller dominates instability. This supports:

• Robust performance under uncertainty
• Controlled degradation under overload
• Predictable behavior under perturbation


8.4 Deployment considerations

For deployment, ICA V1.a requires:

• A mapping from observations \( o_t \) to the input space of UAMC, RMO, and ASM.
• A mapping from actions \( a_t \) to the target environment.
• Initialization of stabilizer parameters and modulator settings.
• Monitoring of key stability indicators (e.g., boundedness of \( x_t \), variance of outputs, constraint violations).


---

9. Canonical V1.a specification

The following elements are considered canonical for ICA V1.a:

1. Operator set:
UAMC, RMO, ICC, PPO, IGO, SLO, TRP, ASM.
2. Modulator set:
SFM, SAM, DRM, WEM, HRM, PBM, PGM, EBM, MEM, IBM, TM, MM.
3. Controller hierarchy:
Local, intermediate, and global controllers as defined in Section 5.
4. Model hierarchy:
1‑D, 2‑D, and 3‑D models as defined in Section 7.
5. Stability layer:
Stabilizer parameters, homeostatic regulation, drift control, and error budgets as defined in Section 8.
6. Loop structure:
Perception → State estimation → Evaluation → Policy/Planning → Action → Feedback, implemented via the operators and modulators above.


Any implementation that:

• Preserves the operator and modulator roles,
• Maintains the controller and model hierarchy,
• Implements the recurrent loop structure,
• And respects the stability and constraint mechanisms,


is considered an instance of ICA V1.a.

---

10. Licensing note

This document is intended to be covered by the repository’s licensing structure, including:

• The code and implementation license (e.g., MIT License).
• The doctrine and documentation license (e.g., CC BY‑ND 4.0).
• The authorship and copyright declaration.


The structure, naming, and interactions of the operators, modulators, controllers, and model hierarchy described here are part of the protected intellectual property of the ICA V1.a specification.

---
