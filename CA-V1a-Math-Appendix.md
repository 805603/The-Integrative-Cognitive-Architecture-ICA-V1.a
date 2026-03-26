ICA V1.a – Mathematical Appendix

1. Notation and Core State

The agent’s internal state at time \(t\) is:

x_t = (b_t, p_t, h_t)


where:

• \(b_t\) is the belief state, including latent variables and uncertainty estimates.
• \(p_t\) is the preference state, encoding goals, constraints, and priorities.
• \(h_t\) is the meta‑state, including historical summaries, reliability measures, and regulatory flags.


Observations follow:

o_t \sim P(o_t \mid a_{t-1}, \text{environment})


Actions are produced by the policy:

a_t = \pi_\theta(x_t, o_t)


---

2. Belief Dynamics

Belief updates follow a general operator:

b_t = \mathcal{B}(b_{t-1}, o_t, a_{t-1})


This operator may be instantiated as:

• Bayesian filtering
• Learned latent dynamics
• Hybrid predictive models


Uncertainty is represented as:

\Sigma_t = \text{Cov}(b_t)


and is used by modulators and regulators throughout the architecture.

---

3. Preference Dynamics

Preferences evolve according to:

p_t = \mathcal{P}(p_{t-1}, c_t, m_t)


where:

• \(c_t\) is contextual input (task, user instruction, deployment constraints).
• \(m_t\) is the meta‑cognitive signal vector.


Preferences may include:

• soft constraints
• hard constraints
• goal weights
• risk sensitivity
• alignment parameters


---

4. Policy Learning Operator

Policy parameters update via:

\theta_{t+1} = \mathcal{L}(\theta_t, x_t, o_t, a_t, r_t, s_t)


where:

• \(r_t\) is the reward or utility signal
• \(s_t\) is the regulatory signal vector


The learning operator is compatible with:

• policy gradient
• actor‑critic
• Q‑learning
• supervised or offline updates


A general gradient‑based form is:

\theta_{t+1} = \theta_t + \alpha_t \nabla_\theta J(\theta_t)


with \(\alpha_t\) modulated by stability and uncertainty modulators.

---

5. Objective Structure

ICA does not collapse all objectives into a single scalar. Instead, it maintains a structured objective vector:

\mathcal{O}_t = ( O^{\text{task}}_t,\; O^{\text{model}}_t,\; O^{\text{reg}}_t,\; O^{\text{meta}}_t )


where:

• \(O^{\text{task}}\) measures task performance
• \(O^{\text{model}}\) measures predictive accuracy and calibration
• \(O^{\text{reg}}\) measures constraint satisfaction
• \(O^{\text{meta}}\) measures meta‑cognitive quality


A regulator or modulator may reweight these channels:

\tilde{\mathcal{O}}_t = W_t \mathcal{O}_t


where \(W_t\) is an adaptive weighting matrix.

---

6. Modulators

A modulator \(\mu\) transforms operator parameters:

\mathcal{L}^\prime = \mu(\mathcal{L}; x_t, \Sigma_t, m_t)


Examples:

Uncertainty Modulator

\alpha_t = f(\Sigma_t)


where \(f\) decreases learning rate or increases exploration when uncertainty is high.

Stability Modulator

\Delta \theta_t \leftarrow \text{clip}(\Delta \theta_t, \epsilon_t)


where \(\epsilon_t\) adapts based on recent volatility.

Alignment Modulator

W_t = g(m_t)


where \(g\) increases weight on alignment‑critical objectives when misalignment signals rise.

---

7. Regulators

Regulators implement explicit control logic.

Action Regulator

a_t^{\text{deploy}} = \mathcal{R}(a_t, x_t, C_t)


where \(C_t\) is the constraint set.

Constraint Satisfaction

Hard constraints require:

a_t^{\text{deploy}} \in \mathcal{A}_{\text{safe}}


Soft constraints introduce penalties:

O^{\text{reg}}_t = -\lambda \cdot \text{violation}(a_t, x_t)


Escalation Thresholds

Let \(E_t\) be an escalation score:

E_t = h(\Sigma_t, m_t, \text{recent errors})


Escalation occurs when:

E_t > \tau_t


where \(\tau_t\) is an adaptive threshold.

---

8. Meta‑Cognitive Signals

Meta‑cognition produces a vector:

m_t = \phi(x_t, \mathcal{O}_t, \text{history})


Typical components include:

• prediction error
• surprise
• regret
• reliability
• distributional shift indicators


These signals feed back into:

• preference updates
• modulators
• regulator thresholds


---

9. Adaptive Threshold Dynamics

Thresholds evolve according to:

\tau_{t+1} = \tau_t + \eta ( \kappa - E_t )


where:

• \(\eta\) is a threshold learning rate
• \(\kappa\) is a target stability level


This creates homeostatic behavior:

• thresholds tighten when the system is unstable
• thresholds relax when the system is reliable


---

10. Deployment Shell Mathematics

Action Filtering

a_t^{\text{deploy}} = 
\begin{cases}
a_t & \text{if } a_t \in \mathcal{A}_{\text{safe}} \\
\text{override}(a_t) & \text{otherwise}
\end{cases}


Rate Limiting

\| a_t - a_{t-1} \| \leq \rho_t


where \(\rho_t\) adapts based on stability.

Capability Restriction

\text{capability}(t) \subseteq \text{capability}(t-1)


when risk increases.

---

11. Summary of Mathematical Guarantees

ICA’s structure supports:

• bounded parameter updates
• adaptive stability control
• explicit constraint satisfaction
• meta‑cognitive correction loops
• compatibility with RL and control theory
• interpretable regulatory behavior


This appendix formalizes the mathematical backbone underlying the ICA V1.a specification.

---
