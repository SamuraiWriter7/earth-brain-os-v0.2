# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-based release flow for schema and reference model development.

---

## [v0.4.0-candidate] - 2026-06-13

### Added

* Introduced **Bidirectional Event Flow** as the core design direction for v0.4.
* Added bidirectional flow schema:

```text
schemas/earth-brain-bidirectional-flow.schema.json
```

* Added bidirectional flow example:

```text
examples/earth-brain-bidirectional-flow.example.yaml
```

* Added bidirectional flow documentation:

```text
docs/bidirectional-event-flow.md
```

* Updated validation script to include bidirectional flow example validation:

```text
scripts/validate_examples.py
```

* Updated README to reflect v0.4 architecture, bidirectional flow schema, documentation, examples, and roadmap.

### Architecture

* Extended v0.3 Lifecycle State Machine with bidirectional layer-to-layer event movement.

```text
v0.2 = Modular Event Architecture
       Layer schemas are separated and referenced through $ref.

v0.3 = Lifecycle State Machine
       Events gain states, transition rules, transition history,
       review boundaries, and terminal states.

v0.4 = Bidirectional Event Flow
       Events move forward and return across layers through feedback,
       trace, review, defense, governance, and human correction paths.
```

* Defined the bidirectional flow schema as a movement companion to the event and lifecycle schemas.

```text
schemas/earth-brain-event.schema.json
= Defines the modular event structure.

schemas/earth-brain-lifecycle.schema.json
= Defines how an event moves through states and transitions.

schemas/earth-brain-bidirectional-flow.schema.json
= Defines how an event moves forward and returns across layers.
```

### Flow Model

* Added canonical flow model:

```text
Earth Brain Bidirectional Event Flow
```

* Added support for:

```text
flow_id
version
flow_model
earth_brain_event_id
lifecycle_id
flow_purpose
active_direction
participating_layers
flow_edges
return_paths
review_boundaries
flow_summary
status
```

### Active Direction

* Added active direction states:

```text
forward
return
feedback_loop
suspended
```

### Participating Layers

* Added supported flow layers:

```text
human_governance_layer
ai_agent_layer
optical_nervous_layer
knowledge_cortex_layer
trace_attribution_layer
royalty_circulation_layer
kazene_regulation_layer
defense_immune_layer
external_system_layer
```

### Flow Edges

* Added directed flow edges with:

```text
edge_id
direction
source_layer
target_layer
signal_type
condition
trace_required
review_required
lifecycle_state_hint
notes
```

* Added edge directions:

```text
forward
return
feedback
```

### Signal Types

* Added supported signal types:

```text
human_intent
ai_reasoning_request
ai_response
trace_update
validation_result
review_request
governance_signal
defense_signal
circulation_signal
regulation_signal
feedback_signal
suspension_signal
```

### Return Paths

* Added return path modeling with:

```text
path_id
return_type
from_layer
to_layer
trigger
requires_human_attention
trace_reference
```

* Added return types:

```text
human_feedback
governance_feedback
defense_feedback
trace_feedback
circulation_feedback
kazene_regulation_feedback
error_feedback
suspension_feedback
```

### Review Boundaries

* Added bidirectional review boundary fields:

```text
human_review_on_return_required
governance_review_on_policy_change_required
defense_review_on_risk_required
trace_required_for_all_edges
automatic_forward_flow_allowed
automatic_return_flow_allowed
```

### Validation

* Updated `scripts/validate_examples.py` to validate:

```text
examples/earth-brain-event.example.yaml
→ schemas/earth-brain-event.schema.json

examples/earth-brain-lifecycle.example.yaml
→ schemas/earth-brain-lifecycle.schema.json

examples/earth-brain-bidirectional-flow.example.yaml
→ schemas/earth-brain-bidirectional-flow.schema.json
```

* Maintained compatibility with the existing GitHub Actions workflow:

```text
.github/workflows/validate-examples.yml
```

### Documentation

* Added `docs/bidirectional-event-flow.md` to explain:

  * purpose of bidirectional flow
  * participating layers
  * active direction
  * forward flow
  * return flow
  * feedback loops
  * defense interruption
  * trace feedback
  * human feedback
  * flow edges
  * signal types
  * return paths
  * review boundaries
  * relationship to v0.2, v0.3, and future v0.5

### Design Notes

* v0.4 does not require a new repository because it builds directly on the v0.2 modular architecture and v0.3 lifecycle model.
* v0.4 turns Earth Brain OS from a one-way event model into a bidirectional circulatory architecture.
* Return paths are treated as first-class schema objects, not informal comments.
* Defense is modeled as an interrupt-and-redirect layer, not merely a blocking wall.
* Human feedback is modeled as part of the system flow, not external to it.

---

## [v0.3.0-candidate] - 2026-06-13

### Added

* Introduced **Lifecycle State Machine** as the core design direction for v0.3.
* Added lifecycle schema:

```text
schemas/earth-brain-lifecycle.schema.json
```

* Added lifecycle example:

```text
examples/earth-brain-lifecycle.example.yaml
```

* Added lifecycle documentation:

```text
docs/event-lifecycle-state-machine.md
```

* Updated validation script to include lifecycle example validation:

```text
scripts/validate_examples.py
```

* Updated README to reflect v0.3 architecture, lifecycle schema, lifecycle documentation, and roadmap.

### Architecture

* Extended v0.2 Modular Event Architecture with lifecycle modeling.

```text
v0.2 = Modular Event Architecture
       Layer schemas are separated and referenced through $ref.

v0.3 = Lifecycle State Machine
       Events gain states, transition rules, transition history,
       review boundaries, and terminal states.
```

### Lifecycle States

* Added the following lifecycle states:

```text
intake
draft
schema_validation
layer_routing
layer_processing
trace_check
human_review
governance_review
defense_review
circulation_review
approved
completed
archived
rejected
suspended
```

### Transition Model

* Added support for transition rules and transition history.

### Review Boundaries

* Added review boundary fields for human, governance, defense, and circulation review.

### Terminal States

* Added terminal states:

```text
completed
archived
rejected
suspended
```

---

## [v0.2.0-candidate] - 2026-06-13

### Added

* Created the initial Earth Brain OS v0.2 repository as a separate modular architecture project.
* Introduced **Modular Event Architecture** as the core design direction for v0.2.
* Added the integrated Earth Brain event schema:

```text
schemas/earth-brain-event.schema.json
```

* Added the first modular layer schema:

```text
schemas/layers/ai-agent-layer.schema.json
```

* Added a minimal valid example event:

```text
examples/earth-brain-event.example.yaml
```

* Added a Python validation script:

```text
scripts/validate_examples.py
```

* Added GitHub Actions validation workflow:

```text
.github/workflows/validate-examples.yml
```

* Added project documentation:

```text
README.md
```

### Architecture

* Defined v0.2 as a transition from a monolithic schema model to a modular `$ref`-based schema architecture.

```text
v0.1 = Monolithic Event Schema
       One integrated event records the full Earth Brain OS structure.

v0.2 = Modular Event Architecture
       Each layer is separated into its own schema, and the integrated event
       references those layers through local $ref paths.
```

* Established the initial modular relationship:

```text
schemas/earth-brain-event.schema.json
└─ layers.ai_agent_layer
   └─ $ref: ./layers/ai-agent-layer.schema.json
```

### AI Agent Layer

* Added the first independent layer module: **AI Agent Layer**.

### Validation

* Added local validation support using:

  * `jsonschema`
  * `pyyaml`

* Added GitHub Actions workflow to validate examples on:

  * push to `main`
  * pull requests to `main`
  * manual workflow dispatch

* Confirmed that the initial validation pipeline passes with the AI Agent Layer module.

---

## Version Direction

### v0.2

**Modular Event Architecture**

Focus:

* schema modularization
* local `$ref` integration
* stable validation pipeline
* staged layer expansion

### v0.3

**Lifecycle State Machine**

Focus:

* event lifecycle states
* transition rules
* transition history
* review boundaries
* terminal states
* lifecycle documentation

### v0.4

**Bidirectional Event Flow**

Focus:

* forward flow
* return flow
* feedback loops
* defense interruption
* trace feedback
* human review return paths

### v0.5

**Event Processing Pipeline**

Focus:

* intake
* validation
* routing
* trace
* review
* circulation
* archive

---

## Repository Status

```text
Version: v0.4.0-candidate
Architecture: Modular Event Architecture + Lifecycle State Machine + Bidirectional Event Flow
Current module: AI Agent Layer
Lifecycle model: Enabled
Bidirectional flow model: Enabled
Validation: Passing
```

