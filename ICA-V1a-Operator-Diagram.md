ICA V1.a – Operator and Architecture Diagram (Text‑Only)

1. High‑Level Architecture

The ICA agent is structured as a set of interacting subsystems arranged in nested control loops:

• World Model
• Preference Model
• Policy System
• Meta‑Cognitive Layer
• Regulatory Shell
• Deployment Safety Envelope


Information flows inward for perception and outward for action, with meta‑cognition and regulation shaping the entire process.

---

2. Text‑Only Architecture Diagram

This diagram uses indentation and arrows to show the full system layout.

ICA Agent
• Observations
 → Perception Operator
  → Feature Representation
   → Belief Update Operator
    → Belief State (bₜ)
     → Uncertainty Estimates (Σₜ)
     → Predictive Model Outputs

• Preferences
 → Context Input (cₜ)
 → Meta‑Cognitive Signals (mₜ)
  → Preference Update Operator
   → Preference State (pₜ)
    → Goals
    → Constraints
     → Hard Constraints
     → Soft Constraints
    → Alignment Parameters

• Policy
 → Policy Input: (bₜ, pₜ, hₜ, oₜ)
  → Policy Operator πθ
   → Proposed Action (aₜ)

• Meta‑Cognition
 → Inputs: performance, prediction error, surprise, reliability, history
  → Meta‑Cognitive Operator
   → Meta‑Signals (mₜ)
   → Threshold Adjustments
   → Regulator Updates

• Regulators
 → Inputs: aₜ, xₜ, constraints, thresholds
  → Action Regulator
   → Safe Action (aₜᵈᵉᵖˡᵒʸ)
  → Capability Regulator
  → Escalation Regulator

• Deployment Shell
 → Action Filtering
 → Rate Limiting
 → Domain Restrictions
 → Logging and Monitoring
 → Human‑in‑the‑Loop Hooks

• Environment
 ← Receives aₜᵈᵉᵖˡᵒʸ
 → Produces new observations oₜ₊₁

---

3. Operator Summary

Belief Operator (𝓑)

Updates latent state and uncertainty from observations and actions.

Preference Operator (𝓟)

Adjusts goals, constraints, and alignment weights based on context and meta‑signals.

Policy Operator (πθ)

Maps internal state and observations to proposed actions.

Learning Operator (𝓛)

Updates policy parameters using reward, regulatory signals, and modulators.

Meta‑Cognitive Operator (φ)

Generates meta‑signals, evaluates reliability, and adjusts thresholds.

Regulatory Operator (𝓡)

Filters, restricts, or overrides actions to enforce safety and capability limits.

---

4. Control Loop Structure

Inner Loop (Task Loop)

Observation → Belief Update → Policy → Action → Environment → Observation

Middle Loop (Learning Loop)

Performance → Learning Operator → Policy Update

Outer Loop (Meta‑Cognitive Loop)

Prediction Error → Meta‑Signals → Preference Update → Modulators → Regulators

Deployment Loop (Safety Loop)

Proposed Action → Regulatory Shell → Safe Action → Environment

---

5. Information Flow Summary

• Perception flows inward.
• Policy flows outward.
• Meta‑cognition flows downward into preferences and modulators.
• Regulators flow upward into action selection.
• Deployment flows around the entire system as a safety envelope.


---

6. Purpose of This Diagram

This operator diagram provides:

• A clear, text‑only representation of ICA’s architecture
• A reference for implementation and academic review
• A structural map for the spec, math appendix, and deployment notes
• A stable, canonical diagram for ICA V1.a


---
