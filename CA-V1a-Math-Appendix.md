ICA V1.a — Mathematical Appendix (Canonical Specification, 2026 Revision)

1. Core State and System Variables
The agent maintains a structured internal state:
    x_t = (ŝ_t, θ_t, Σ_t, m_t)

where:
• ŝ_t is the estimated latent state (SES output)
• θ_t are internal model parameters (MUS parameters)
• Σ_t is the uncertainty estimate associated with ŝ_t
• m_t is the meta‑cognitive signal vector

Observations follow:
    o_t ~ P(o_t | a_{t-1}, environment)

Actions are produced by:
    a_t = π(x_t, o_t)

2. State Estimation (SES)
The belief estimate evolves according to:
    ŝ_t = SES(o_{1:t}, a_{1:t-1}; θ_t)

Uncertainty is tracked as:
    Σ_t = Cov(ŝ_t)

3. Information‑Gain Strategy (IGS)
Expected information gain from action a:
    IGS_t(a) = E[ I(ŝ_{t+1}; o_{t+1} | a, ŝ_t) ]

4. Risk‑Management System (RMS) with Tail‑Risk Term
Risk is evaluated as:
    RMS_t(a) = E[C(ŝ_{t+1}, a)] + λ_tail · CVaR_α(C)

5. Model‑Update System (MUS)
Internal model parameters update via:
    θ_{t+1} = MUS(θ_t, o_{t+1}, a_t)

6. Unified Objective
Weights:
• α_t = exploration weight
• β_t = risk weight
• γ_t = action‑cost weight

Objective:
    J_t(a) = α_t·IGS_t(a) − β_t·RMS_t(a) − γ_t·Cost(a)

Raw action:
    a_t_raw = argmax_a J_t(a)

7. Integrative Coherence Condition (ICC)
Coherence score:
    κ_t = ICC(ŝ_t, θ_t, IGS_t, RMS_t)

Condition:
• κ_t ≥ τ_ICC → coherent
• κ_t < τ_ICC → controllers intervene

8. Dual Error Channels
Model error:
    E_model_t = || ŝ_{t+1} − s_{t+1} ||

Environment drift:
    E_env_t = D_KL( p(o_t) || p(o_{t−1}) )

Routing:
• High E_model_t → MUS/IGO correction
• High E_env_t → TRP + reflex arc

9. Meta‑Objective Discrepancy Signal
Discrepancy:
    D_t = distance(realized_outcomes_t, acceptable_outcome_band)

ASM update:
    (α_{t+1}, β_{t+1}, γ_{t+1}) = ASM(α_t, β_t, γ_t, volatility_t, D_t)

10. Controller Stack

10.1 Unified Action‑Model Controller (UAMC)
    a_t_UAMC = UAMC(a_t_raw, κ_t, ŝ_t, θ_t)

10.2 Threat‑Response Protocol (TRP)
Aggressive mode triggers when:
    κ_t < τ_ICC_aggr OR w_t > w_max OR E_env_t high

Parameter shifts:
    α_t_aggr = λ_α α_t
    β_t_aggr = λ_β β_t
    γ_t_aggr = λ_γ γ_t

Adjusted action:
    a_t_TRP = TRP(a_t_UAMC, κ_t, w_t, E_env_t)

10.3 Adaptive Stability Mechanism (ASM)
    (α, β, γ) updated using volatility_t and D_t

10.4 Proportional Policy Optimizer (PPO)
Local refinement of a_t.

10.5 Iterative Gradient Operator (IGO)
    θ_{t+1} = θ_t − η_θ ∇_θ L(θ_t)

10.6 Risk‑Mitigation Operator (RMO)
    J_t_RMO(a) = J_t(a) − δ_t·max(0, RMS_t(a) − r_max)

10.7 Stability‑Loss Operator (SLO)
    ℓ_t = SLO(κ_{t−k:t}, volatility_{t−k:t})

If ℓ_t > ℓ_crit → reflex arc and/or TRP

11. Modulators

11.1 Clarity Modulator
    IGS_t_eff(a) = c_t · IGS_t(a)
    Var(SES)_eff = Var(SES) / c_t

11.2 Temporal Stability Modulator
    η_{θ,t+1} = f_time(η_{θ,t}, volatility_t)
    T_{t+1} = f_window(T_t, volatility_t)

12. Resource‑Stability Controller (RSC)
Resource signal:
    R_t = available compute/time/bandwidth

If R_t < R_min:
    α_t → α_min
    β_t → β_max
    γ_t → γ_max
    η_θ reduced
    A → A_safe

13. Reflex Arc
Trigger:
    E_t > E_crit

Actions:
• α_t reduced
• β_t increased
• γ_t increased
• c_t increased

Exit condition:
    E_t ≤ E_stable AND ℓ_t ≤ ℓ_crit

14. Mode Variable
Discrete mode:
    m_t ∈ { normal, defensive, reflex }

15. Suspended‑Aliveness Diagnostic Regime
    R_stable = {
        (κ_t, volatility_t, E_t) |
        κ_t ≥ τ_ICC_stable,
        volatility_t ≤ v_stable,
        E_t ≤ E_stable
    }

16. Formal Degradation Invariant
If:
    κ_t → 0 OR volatility_t → ∞ OR R_t → 0

Then:
    α_t → α_min
    β_t → β_max
    γ_t → γ_max
    A → A_safe

17. Mathematical Guarantees
The architecture ensures:
• bounded parameter updates
• adaptive stability control
• explicit constraint satisfaction
• meta‑cognitive correction loops
• compatibility with RL and control theory
• interpretable regulatory behavior
• guaranteed controlled‑conservative degradation under stress
