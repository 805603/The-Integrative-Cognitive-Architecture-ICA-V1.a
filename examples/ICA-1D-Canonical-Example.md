
ICA V1.a — Canonical 1‑D Toy Environment
A minimal, interpretable demonstration of ICA dynamics

1. Purpose of the 1‑D Model
The 1‑D environment is the simplest possible setting that still expresses the full internal logic of ICA: uncertainty, awareness, curiosity, compassion, unified policy behavior, regulator activation, and threshold dynamics. It is the anchor example for teaching, intuition-building, and mathematical clarity.
2. Environment Definition
State:
The agent occupies a continuous 1‑D position: x_t (a real number).


Dynamics:
The environment evolves with Gaussian noise:
x_(t+1) = x_t + a_t + noise

Belief:
The agent maintains a Gaussian belief with mean (mu_t) and variance (Sigma_t).
This belief updates using standard Bayesian filtering.

1. ICA Operators in 1‑D


Awareness:
Awareness is the inverse of uncertainty:
A_t = 1 / (1 + Sigma_t)

Curiosity:
Curiosity is the expected reduction in uncertainty:
C_t = expected value of (Sigma_t - Sigma_(t+1))

Compassion:
A penalty for entering a danger zone.
If the agent’s estimated position is inside a danger region, compassion adds a negative term.

Unified Objective:
The combined objective in 1‑D is a weighted sum of:
• awareness
• curiosity
• compassion
• action cost (penalizing large actions)

1. Policy Behavior
The policy chooses actions that maximize the unified objective while respecting:
• regulator constraints
• uncertainty thresholds
• safe‑mode triggers
• capability limits
2. Regulators in 1‑D


Hard constraints:
• maximum step size
• forbidden regions
• safety boundaries

Soft constraints:
• risk sensitivity
• uncertainty shaping
• compassion weighting

Escalation:
Triggered by uncertainty spikes, repeated constraint violations, or rising prediction error.

Safe‑mode:
When activated:
• exploration decreases
• step size shrinks
• curiosity is dampened
• compassion weight increases

1. Why the 1‑D Model Matters
The 1‑D environment is:
• analytically clean
• mathematically transparent
• easy to visualize
• ideal for proofs
• ideal for teaching
• ideal for debugging
• ideal for demonstrating ICA’s internal logic


This is the canonical example for ICA V1.a.
