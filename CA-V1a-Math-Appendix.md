ICA V1.a — Mathematical Appendix (Canonical Specification, 2026 Revision)

Core State and System Variables The agent maintains a structured internal state: x_t = (ŝ_t, θ_t, Σ_t, m_t)
where: • ŝ_t is the estimated latent state (SES output) • θ_t are internal model parameters (MUS parameters) • Σ_t is the uncertainty estimate associated with ŝ_t • m_t is the meta‑cognitive signal vector

Observations follow: o_t ~ P(o_t | a_{t-1}, environment)

Actions are produced by: a_t = π(x_t, o_t)

State Estimation (SES) The belief estimate evolves according to: ŝ_t = SES(o_{1:t}, a_{1:t-1}; θ_t)
Uncertainty is tracked as: Σ_t = Cov(ŝ_t)

Information‑Gain Strategy (IGS) Expected information gain from action a: IGS_t(a) = E[ I(ŝ_{t+1}; o_{t+1} | a, ŝ_t) ]

Risk‑Management System (RMS) with Tail‑Risk Term Risk is evaluated as: RMS_t(a) = E[C(ŝ_{t+1}, a)] + λ_tail · CVaR_α(C)

Model‑Update System (MUS) Internal model parameters update via: θ_{t+1} = MUS(θ_t, o_{t+1}, a_t)

Unified Objective Weights: • α_t = exploration weight • β_t = risk weight • γ_t = action‑cost weight

Objective: J_t(a) = α_t·IGS_t(a) − β_t·RMS_t(a) − γ_t·Cost(a)

Raw action: a_t_raw = argmax_a J_t(a)

Integrative Coherence Condition (ICC) Coherence score: κ_t = ICC(ŝ_t, θ_t, IGS_t, RMS_t)
Condition: • κ_t ≥ τ_ICC → coherent • κ_t < τ_ICC → controllers intervene

Dual Error Channels Model error: E_model_t = || ŝ_{t+1} − s_{t+1} ||
Environment drift: E_env_t = D_KL( p(o_t) || p(o_{t−1}) )

Routing: • High E_model_t → MUS/IGO correction • High E_env_t → TRP + reflex arc

Meta‑Objective Discrepancy Signal Discrepancy: D_t = distance(realized_outcomes_t, acceptable_outcome_band)
ASM update: (α_{t+1}, β_{t+1}, γ_{t+1}) = ASM(α_t, β_t, γ_t, volatility_t, D_t)

Controller Stack
10.1 Unified Action‑Model Controller (UAMC) a_t_UAMC = UAMC(a_t_raw, κ_t, ŝ_t, θ_t)

10.2 Threat‑Response Protocol (TRP) Aggressive mode triggers when: κ_t < τ_ICC_aggr OR w_t > w_max OR E_env_t high

Parameter shifts: α_t_aggr = λ_α α_t β_t_aggr = λ_β β_t γ_t_aggr = λ_γ γ_t

Adjusted action: a_t_TRP = TRP(a_t_UAMC, κ_t, w_t, E_env_t)

10.3 Adaptive Stability Mechanism (ASM) (α, β, γ) updated using volatility_t and D_t

10.4 Proportional Policy Optimizer (PPO) Local refinement of a_t.

10.5 Iterative Gradient Operator (IGO) θ_{t+1} = θ_t − η_θ ∇_θ L(θ_t)

10.6 Risk‑Mitigation Operator (RMO) J_t_RMO(a) = J_t(a) − δ_t·max(0, RMS_t(a) − r_max)

10.7 Stability‑Loss Operator (SLO) ℓ_t = SLO(κ_{t−k:t}, volatility_{t−k:t})

If ℓ_t > ℓ_crit → reflex arc and/or TRP

Modulators
11.1 Clarity Modulator IGS_t_eff(a) = c_t · IGS_t(a) Var(SES)_eff = Var(SES) / c_t

11.2 Temporal Stability Modulator η_{θ,t+1} = f_time(η_{θ,t}, volatility_t) T_{t+1} = f_window(T_t, volatility_t)

Resource‑Stability Controller (RSC) Resource signal: R_t = available compute/time/bandwidth
If R_t < R_min: α_t → α_min β_t → β_max γ_t → γ_max η_θ reduced A → A_safe

Reflex Arc Trigger: E_t > E_crit
Actions: • α_t reduced • β_t increased • γ_t increased • c_t increased

Exit condition: E_t ≤ E_stable AND ℓ_t ≤ ℓ_crit

Mode Variable Discrete mode: m_t ∈ { normal, defensive, reflex }

Suspended‑Aliveness Diagnostic Regime R_stable = { (κ_t, volatility_t, E_t) | κ_t ≥ τ_ICC_stable, volatility_t ≤ v_stable, E_t ≤ E_stable }

Formal Degradation Invariant If: κ_t → 0 OR volatility_t → ∞ OR R_t → 0

Then: α_t → α_min β_t → β_max γ_t → γ_max A → A_safe

Mathematical Guarantees The architecture ensures: • bounded parameter updates • adaptive stability control • explicit constraint satisfaction • meta‑cognitive correction loops • compatibility with RL and control theory • interpretable regulatory behavior • guaranteed controlled‑conservative degradation under stress V1.a – Mathematical Appendix

Notation and Core State

The agent’s internal state at time (t) is:

x_t = (b_t, p_t, h_t)

where:

• (b_t) is the belief state, including latent variables and uncertainty estimates. • (p_t) is the preference state, encoding goals, constraints, and priorities. • (h_t) is the meta‑state, including historical summaries, reliability measures, and regulatory flags.

Observations follow:

o_t \sim P(o_t \mid a_{t-1}, \text{environment})

Actions are produced by the policy:

a_t = \pi_\theta(x_t, o_t)

Belief Dynamics
Belief updates follow a general operator:

b_t = \mathcal{B}(b_{t-1}, o_t, a_{t-1})

This operator may be instantiated as:

• Bayesian filtering • Learned latent dynamics • Hybrid predictive models

Uncertainty is represented as:

\Sigma_t = \text{Cov}(b_t)

and is used by modulators and regulators throughout the architecture.

Preference Dynamics
Preferences evolve according to:

p_t = \mathcal{P}(p_{t-1}, c_t, m_t)

where:

• (c_t) is contextual input (task, user instruction, deployment constraints). • (m_t) is the meta‑cognitive signal vector.

Preferences may include:

• soft constraints • hard constraints • goal weights • risk sensitivity • alignment parameters

Policy Learning Operator
Policy parameters update via:

\theta_{t+1} = \mathcal{L}(\theta_t, x_t, o_t, a_t, r_t, s_t)

where:

• (r_t) is the reward or utility signal • (s_t) is the regulatory signal vector

The learning operator is compatible with:

• policy gradient • actor‑critic • Q‑learning • supervised or offline updates

A general gradient‑based form is:

\theta_{t+1} = \theta_t + \alpha_t \nabla_\theta J(\theta_t)

with (\alpha_t) modulated by stability and uncertainty modulators.

Objective Structure
ICA does not collapse all objectives into a single scalar. Instead, it maintains a structured objective vector:

\mathcal{O}_t = ( O^{\text{task}}_t,; O^{\text{model}}_t,; O^{\text{reg}}_t,; O^{\text{meta}}_t )

where:

• (O^{\text{task}}) measures task performance • (O^{\text{model}}) measures predictive accuracy and calibration • (O^{\text{reg}}) measures constraint satisfaction • (O^{\text{meta}}) measures meta‑cognitive quality

A regulator or modulator may reweight these channels:

\tilde{\mathcal{O}}_t = W_t \mathcal{O}_t

where (W_t) is an adaptive weighting matrix.

Modulators
A modulator (\mu) transforms operator parameters:

\mathcal{L}^\prime = \mu(\mathcal{L}; x_t, \Sigma_t, m_t)

Examples:

Uncertainty Modulator

\alpha_t = f(\Sigma_t)

where (f) decreases learning rate or increases exploration when uncertainty is high.

Stability Modulator

\Delta \theta_t \leftarrow \text{clip}(\Delta \theta_t, \epsilon_t)

where (\epsilon_t) adapts based on recent volatility.

Alignment Modulator

W_t = g(m_t)

where (g) increases weight on alignment‑critical objectives when misalignment signals rise.

Regulators
Regulators implement explicit control logic.

Action Regulator

a_t^{\text{deploy}} = \mathcal{R}(a_t, x_t, C_t)

where (C_t) is the constraint set.

Constraint Satisfaction

Hard constraints require:

a_t^{\text{deploy}} \in \mathcal{A}_{\text{safe}}

Soft constraints introduce penalties:

O^{\text{reg}}_t = -\lambda \cdot \text{violation}(a_t, x_t)

Escalation Thresholds

Let (E_t) be an escalation score:

E_t = h(\Sigma_t, m_t, \text{recent errors})

Escalation occurs when:

E_t > \tau_t

where (\tau_t) is an adaptive threshold.

Meta‑Cognitive Signals
Meta‑cognition produces a vector:

m_t = \phi(x_t, \mathcal{O}_t, \text{history})

Typical components include:

• prediction error • surprise • regret • reliability • distributional shift indicators

These signals feed back into:

• preference updates • modulators • regulator thresholds

Adaptive Threshold Dynamics
Thresholds evolve according to:

\tau_{t+1} = \tau_t + \eta ( \kappa - E_t )

where:

• (\eta) is a threshold learning rate • (\kappa) is a target stability level

This creates homeostatic behavior:

• thresholds tighten when the system is unstable • thresholds relax when the system is reliable

Deployment Shell Mathematics
Action Filtering

a_t^{\text{deploy}} = \begin{cases} a_t & \text{if } a_t \in \mathcal{A}_{\text{safe}} \ \text{override}(a_t) & \text{otherwise} \end{cases}

Rate Limiting

| a_t - a_{t-1} | \leq \rho_t

where (\rho_t) adapts based on stability.

Capability Restriction

\text{capability}(t) \subseteq \text{capability}(t-1)

when risk increases.

Summary of Mathematical Guarantees
ICA’s structure supports:

• bounded parameter updates • adaptive stability control • explicit constraint satisfaction • meta‑cognitive correction loops • compatibility with RL and control theory • interpretable regulatory behavior

This appendix formalizes the mathematical backbone underlying the ICA V1.a specification.

