
# ICA V1.a — Mathematical Appendix (Canonical Specification, 2026 Revision)

This appendix provides the formal mathematical foundations of ICA V1.a. It defines the system state, operator equations, coherence constraints, stability conditions, and the unified objective in its complete analytical form. All notation is aligned with the ICA V1.a Technical Specification.

---

## 1. Core State and System Variables

The agent maintains a structured internal state:
```blockmath
x_t = (\hat{s}_t, \theta_t, \Sigma_t, m_t)
```

Where:
- `\( \hat{s}_t \)`: latent state estimate (SES output)  
- `\( \theta_t \)`: internal model parameters (MUS parameters)  
- `\( \Sigma_t \)`: uncertainty estimate associated with `\( \hat{s}_t \)`  
- `\( m_t \)`: meta‑cognitive mode variable  

Observations follow:
```blockmath
o_t \sim P(o_t \mid a_{t-1}, \text{environment})
```

Actions are produced by:
```blockmath
a_t = \pi(x_t, o_t)
```

---

## 2. State Estimation System (SES)

Belief update:
```blockmath
\hat{s}_t = SES(o_{1:t}, a_{1:t-1}; \theta_t)
```

Uncertainty propagation:
```blockmath
\Sigma_t = \mathrm{Cov}(\hat{s}_t)
```

---

## 3. Information‑Gain Strategy (IGS)

Expected information gain from action `\( a \)`:
```blockmath
IGS_t(a) = \mathbb{E}\left[ I(\hat{s}_{t+1}; o_{t+1} \mid a, \hat{s}_t) \right]
```

---

## 4. Risk‑Management System (RMS)

Risk expectation:
```blockmath
RMS_t(a) = \mathbb{E}[C(\hat{s}_{t+1}, a)]
```

Tail‑risk penalty:
```blockmath
RMS_t(a) \leftarrow RMS_t(a) + \lambda_{\text{tail}} \cdot CVaR_\alpha(C)
```

---

## 5. Model‑Update System (MUS)

Parameter update:
```blockmath
\theta_{t+1} = MUS(\theta_t, o_{t+1}, a_t)
```

Gradient form:
```blockmath
\theta_{t+1} = \theta_t - \eta_\theta \nabla_\theta L(\theta_t)
```

---

## 6. Unified Objective Function

Weights:
- `\( \alpha_t \)`: exploration  
- `\( \beta_t \)`: risk  
- `\( \gamma_t \)`: action cost  

Unified objective:
```blockmath
J_t(a) = \alpha_t \cdot IGS_t(a) - \beta_t \cdot RMS_t(a) - \gamma_t \cdot Cost(a)
```

Raw action:
```blockmath
a_{t}^{raw} = \arg\max_a J_t(a)
```

---

## 7. Integrative Coherence Condition (ICC)

Coherence score:
```blockmath
\kappa_t = ICC(\hat{s}_t, \theta_t, IGS_t, RMS_t)
```

Coherence condition:
- `\( \kappa_t \ge \tau_{ICC} \)`: coherent  
- `\( \kappa_t < \tau_{ICC} \)`: controllers intervene  

---

## 8. Global Coherence Constraint (GCC)

Global alignment penalty:
```blockmath
GCC_t = \lambda_{GCC} \cdot D(\hat{s}_t, \theta_t)
```

Unified objective with GCC:
```blockmath
J_t^{full}(a) = J_t(a) - GCC_t
```

---

## 9. Dual Error Channels

Model error:
```blockmath
E^{model}_t = \| \hat{s}_{t+1} - s_{t+1} \|
```

Environment drift:
```blockmath
E^{env}_t = D_{KL}(p(o_t) \parallel p(o_{t-1}))
```

Routing:
- High `\( E^{model}_t \)` → MUS/IGO  
- High `\( E^{env}_t \)` → TRP + reflex arc  

---

## 10. Discrepancy Signal

Meta‑objective discrepancy:
```blockmath
D_t = d(\text{realized outcomes}_t, \text{acceptable band})
```

ASM update:
```blockmath
(\alpha_{t+1}, \beta_{t+1}, \gamma_{t+1}) = ASM(\alpha_t, \beta_t, \gamma_t, volatility_t, D_t)
```

---

## 11. Controller Stack

### 11.1 Unified Action‑Model Controller (UAMC)
```blockmath
a_t^{UAMC} = UAMC(a_t^{raw}, \kappa_t, \hat{s}_t, \theta_t)
```

### 11.2 Threat‑Response Protocol (TRP)

Aggressive mode triggers when:
```blockmath
\kappa_t < \tau_{ICC}^{aggr} \quad \text{or} \quad w_t > w_{max} \quad \text{or} \quad E^{env}_t \text{ high}
```

Parameter shifts:
```blockmath
\alpha_t^{aggr} = \lambda_\alpha \alpha_t,\quad
\beta_t^{aggr} = \lambda_\beta \beta_t,\quad
\gamma_t^{aggr} = \lambda_\gamma \gamma_t
```

Adjusted action:
```blockmath
a_t^{TRP} = TRP(a_t^{UAMC}, \kappa_t, w_t, E^{env}_t)
```

### 11.3 Adaptive Stability Mechanism (ASM)
Updates `\( (\alpha, \beta, \gamma) \)` using volatility and discrepancy.

### 11.4 Proportional Policy Optimizer (PPO)
Local refinement of `\( a_t \)`.

### 11.5 Iterative Gradient Operator (IGO)
```blockmath
\theta_{t+1} = \theta_t - \eta_\theta \nabla_\theta L(\theta_t)
```

### 11.6 Risk‑Mitigation Operator (RMO)
```blockmath
J_t^{RMO}(a) = J_t(a) - \delta_t \cdot \max(0, RMS_t(a) - r_{max})
```

### 11.7 Stability‑Loss Operator (SLO)
```blockmath
\ell_t = SLO(\kappa_{t-k:t}, volatility_{t-k:t})
```

If:
```blockmath
\ell_t > \ell_{crit}
```
then reflex arc and/or TRP activate.

---

## 12. Modulators

### 12.1 Clarity Modulator
```blockmath
IGS_t^{eff}(a) = c_t \cdot IGS_t(a)
```
```blockmath
Var(SES)_{eff} = \frac{Var(SES)}{c_t}
```

### 12.2 Temporal Stability Modulator
```blockmath
\eta_{\theta,t+1} = f_{time}(\eta_{\theta,t}, volatility_t)
```
```blockmath
T_{t+1} = f_{window}(T_t, volatility_t)
```

---

## 13. Resource‑Stability Controller (RSC)

Resource signal:
```blockmath
R_t = \text{available compute/time/bandwidth}
```

If `\( R_t < R_{min} \)`:
```blockmath
\alpha_t \rightarrow \alpha_{min},\quad
\beta_t \rightarrow \beta_{max},\quad
\gamma_t \rightarrow \gamma_{max},\quad
\eta_\theta \rightarrow \eta_{\theta, safe}
```

---

## 14. Reflex Arc

Trigger:
```blockmath
E_t > E_{crit}
```

Actions:
- `\( \alpha_t \)` reduced  
- `\( \beta_t \)` increased  
- `\( \gamma_t \)` increased  
- `\( c_t \)` increased  

Exit condition:
```blockmath
E_t \le E_{stable} \quad \text{and} \quad \ell_t \le \ell_{crit}
```

---

## 15. Mode Variable

Discrete mode:
```blockmath
m_t \in \{ normal, defensive, reflex \}
```

---

## 16. Suspended‑Aliveness Diagnostic Regime

Stability region:
```blockmath
R_{stable} = \{ (\kappa_t, volatility_t, E_t) \mid \kappa_t \ge \tau_{ICC}^{stable},\; volatility_t \le v_{stable},\; E_t \le E_{stable} \}
```

---

## 17. Degradation Invariant

If:
```blockmath
\kappa_t \rightarrow 0 \quad \text{or} \quad volatility_t \rightarrow \infty \quad \text{or} \quad R_t \rightarrow 0
```

Then:
```blockmath
\alpha_t \rightarrow \alpha_{min},\quad
\beta_t \rightarrow \beta_{max},\quad
\gamma_t \rightarrow \gamma_{max},\quad
A \rightarrow A_{safe}
```

---

## 18. Mathematical Guarantees

The architecture ensures:
- bounded parameter updates  
- adaptive stability control  
- explicit constraint satisfaction  
- meta‑cognitive correction loops  
- compatibility with RL and control theory  
- interpretable regulatory behavior  
- guaranteed controlled‑conservative degradation under stress  

---

End of Mathematical Appendix
