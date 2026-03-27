
ICA V1.a – Deployment Notes

Purpose of This Document
These notes describe how ICA behaves in real‑world deployment. They explain how the architecture transitions from training to operation, how regulators enforce constraints, how meta‑cognition stabilizes behavior, how the discrepancy signal drives mode transitions, and how the deployment shell ensures safety, reliability, and interpretability. This document is the operational counterpart to the specification and mathematical appendix.

Deployment Architecture Overview
ICA’s deployment behavior is governed by four interacting layers:

Policy Layer
Generates proposed actions based on beliefs, preferences, observations, and structural gradients.

Regulatory Layer
Filters, restricts, or overrides actions to enforce constraints, stabilize behavior, and prevent incoherent or unsafe trajectories.

Meta‑Cognitive Layer
Monitors reliability, uncertainty, discrepancy, prediction error, and regulator activity. Adjusts thresholds, capability levels, and regulator strictness.

Deployment Shell
Wraps the entire system with safety controls, logging, rate limiting, capability envelopes, and domain restrictions.

These layers form a nested control structure that ensures stable, aligned behavior under uncertainty.

Action Path in Deployment
The action path in deployment differs from training.

3.1 Proposed Action
The policy produces an action:
• based on belief state  
• shaped by preferences and priors  
• influenced by structural gradients  
• modulated by meta‑signals  

This action is not executed directly.

3.2 Regulatory Filtering
The action is passed through:
• hard constraint checks  
• soft constraint penalties  
• capability restrictions  
• discrepancy‑weighted regulators  
• mode‑dependent filters  
• escalation thresholds  

If the action violates constraints, it is modified or replaced.

3.3 Deployment Shell Enforcement
The deployment shell applies:
• rate limiting  
• domain restrictions  
• safety overrides  
• capability envelope enforcement  
• logging and monitoring  

3.4 Final Action
Only after passing all layers is the action sent to the environment.

Hard and Soft Constraints

4.1 Hard Constraints
These must never be violated. Examples include:
• domain boundaries  
• safety rules  
• forbidden actions  
• capability ceilings and floors  

If a proposed action violates a hard constraint, it is replaced with a safe alternative.

4.2 Soft Constraints
These shape behavior without absolute prohibition. Violations incur penalties or trigger regulator adjustments.

Soft constraints influence:
• risk sensitivity  
• alignment weights  
• preference shaping  
• uncertainty inflation  

ICC and the Discrepancy Signal
ICA uses the Integrative Coherence Condition (ICC) to measure internal consistency.

The discrepancy signal is defined as:
D_t = || ICC(x_t) ||

Deployment behavior depends on D_t:
• low D_t → normal operation  
• moderate D_t → increased sampling, regulator activation  
• high D_t → escalation, capability reduction, or safe‑mode  
• extreme D_t → SAFE2 (Black Swan protection)  

D_t is logged continuously and drives mode transitions.

Mode System in Deployment
ICA operates in three modes:

Normal Mode
• full capability  
• balanced exploration  
• standard regulator strictness  

Aggressive‑Mode
• triggered when uncertainty is high but risk is low  
• increases exploration  
• relaxes some regulators  
• uses a hysteresis window to prevent rapid switching  

Safe‑Mode (SAFE1)
• triggered by high discrepancy, rising risk, or repeated violations  
• reduces capability  
• tightens thresholds  
• suppresses exploration  
• increases regulator strictness  

SAFE2 (Black Swan Mode)
• triggered by extreme discrepancy, catastrophic instability, or severe distributional shift  
• exploration disabled  
• learning paused  
• only low‑risk actions allowed  
• hard action suppression enabled  

Mode transitions use hysteresis to prevent oscillation.

Reliability Engine
The reliability engine modulates:
• threshold tightening  
• uncertainty inflation  
• regulator activation  
• capability restriction  
• exploration damping  

Low reliability increases caution; high reliability restores capability.

Oscillation Detection and Suppression
ICA monitors for oscillatory behavior using a rolling window (e.g., 1000ms).

If oscillation is detected:
• regulators tighten  
• thresholds increase  
• exploration decreases  
• capability may be reduced  
• mode may shift to SAFE1  

Persistent oscillation triggers SAFE2.

Reflex Arc and Embodied Stability Layer
ICA includes a reflex arc for rapid stabilization.

Trigger Conditions
• rising discrepancy  
• sudden uncertainty spikes  
• regulator saturation  
• oscillation onset  

Physical Cue
• grounding signal  
• embodied stability cue  
• suspended‑aliveness anchor  

Completion Signals
• clarity restoration  
• discrepancy reduction  
• regulator normalization  

The reflex arc ensures rapid stabilization under stress.

Adaptive Thresholds in Deployment

6.1 Threshold Inputs
Thresholds depend on:
• uncertainty  
• reliability  
• recent errors  
• discrepancy  
• regulator activity  
• mode state  
• oscillation detection  

6.2 Threshold Dynamics
Thresholds tighten when instability rises and relax when stability returns. This creates homeostatic behavior that prevents runaway dynamics.

Capability Management

7.1 Capability Envelope
Capabilities are bounded by:
• domain limits  
• safety ceilings  
• minimum capability floors  

7.2 Capability Reduction
Capabilities are reduced when:
• risk increases  
• uncertainty rises  
• discrepancy grows  
• regulators activate frequently  
• reliability decreases  

7.3 Capability Restoration
Capabilities are restored when:
• stability improves  
• uncertainty decreases  
• prediction error normalizes  
• reliability increases  

Logging and Monitoring
The deployment shell logs:
• proposed actions  
• final actions  
• regulator events  
• threshold changes  
• mode transitions  
• discrepancy levels  
• oscillation detection  
• SAFE1/SAFE2 entries  
• uncertainty levels  
• meta‑cognitive summaries  
• constraint violations  

These logs support:
• debugging  
• auditing  
• safety analysis  
• performance evaluation  
• academic reproducibility  

Human‑in‑the‑Loop Integration
ICA supports human oversight at multiple levels:
• approval gates  
• override mechanisms  
• shutdown triggers  
• escalation notifications  

Human‑in‑the‑loop is optional but recommended for high‑risk domains.

Distributional Shift Handling
ICA detects distributional shift through:
• prediction error  
• surprise metrics  
• uncertainty spikes  
• discrepancy increases  
• regulator activity patterns  
• reliability drops  

When shift is detected:
• thresholds tighten  
• learning slows  
• exploration decreases  
• capability may be reduced  
• SAFE1 or SAFE2 may activate  

Deployment Summary
A correct ICA deployment must:
• filter all actions through regulators  
• enforce hard and soft constraints  
• adapt thresholds based on stability  
• use discrepancy‑driven mode transitions  
• support escalation and safe‑mode  
• maintain logs and monitoring  
• integrate human oversight when needed  
• wrap the entire system in a safety envelope  
• enforce capability envelopes  
• suppress oscillation  
• stabilize via the reflex arc  

These notes complete the operational foundation of ICA V1.a.
