
# How to Read ICA V1.a

This guide orients new readers to the structure, logic, and reading order of the Integrative Cognitive Architecture (ICA V1.a). The goal is to make the system accessible to engineers, researchers, and reviewers encountering it for the first time.

## What ICA V1.a Represents

ICA V1.a is a coherence‑first cognitive architecture. Every component—operators, modulators, regulators, diagnostics, and embodied feedback—exists to maintain stable, adaptive cognition. The system is designed to be readable without requiring philosophical background or prior exposure to cognitive architectures.

## Recommended Reading Order

A clear reading path helps new readers understand the architecture without getting lost in details.

### 1. Start with the Vertical Stack
Begin with `architecture/vertical-stack.md`. This file provides the full hierarchy of the system and shows how each layer relates to the others. It establishes the mental model needed for everything else.

### 2. Read the OS Layer
`architecture/os-layer.md` explains the coherence engine that anchors the entire architecture. Understanding this layer makes the rest of the system intuitive.

### 3. Move Through the Cognitive Layers
Read the files in this order:
- `operators.md`
- `modulators.md`
- `regulators.md`
- `diagnostics.md`

This sequence follows the natural flow of cognitive signals from generation to refinement to stabilization to monitoring.

### 4. Study the Embodied Components
Two files define the architecture’s grounding and stability:
- `reflex-arc.md`
- `suspended-aliveness.md`

These explain how ICA V1.a maintains embodied coherence and recovers from destabilization.

### 5. Review the Module Admission Rule
`module-admission-rule.md` describes how new components are evaluated for coherence and safety before being integrated into the system.

## How to Use the Diagrams

The `diagrams/` folder contains text specifications for all system diagrams. These are not images but structured descriptions that can be rendered visually later.

The diagrams help readers:
- visualize the vertical stack  
- understand operator flow  
- see how regulators interact  
- follow the coherence loop  
- understand the reflex arc  

Reading the diagrams after the architecture files reinforces the system’s structure.

## How the System Maintains Coherence

ICA V1.a uses a layered approach:
- Operators generate cognitive signals.  
- Modulators adjust intensity, timing, and sensitivity.  
- Regulators enforce safety and stability.  
- Diagnostics monitor coherence and noise.  
- The reflex arc provides fast embodied feedback.  
- The suspended‑aliveness baseline serves as the target state.  
- The OS Layer integrates everything into global coherence.

Understanding this loop is essential for interpreting the architecture as a whole.

## How to Interpret the Suspended‑Aliveness Baseline

This baseline is the architecture’s optimal coherence state. It is not a metaphor or philosophical construct; it is a functional stability condition. All layers orient toward maintaining or returning to this state.

## Licensing and Usage

This documentation is governed by the repository’s dual‑license structure:
- **LICENSE** covers the architecture and technical content.  
- **LICENSE-DOCS** covers all documentation, including this guide.  
- **COPYRIGHT** asserts authorship and ownership.  
- **NOTICE** provides required legal notices for redistribution.

Readers should consult these files before reusing or adapting any part of the system.

## How to Navigate the Repository

The repository is organized for clarity:
- `architecture/` contains the full technical specification.  
- `diagrams/` contains diagram specifications.  
- `docs/` contains licensing, notices, and reading guides.  

Each folder is self‑contained and designed to be readable independently, but the recommended reading order provides the smoothest learning curve.

Understanding how you want new readers to experience ICA V1.a helps refine this guide further.
