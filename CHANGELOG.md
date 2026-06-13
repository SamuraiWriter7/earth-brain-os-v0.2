# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-based release flow for schema and reference model development.

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

* Defined the lifecycle schema as a procedural companion to the modular event schema.

```text
schemas/earth-brain-event.schema.json
= Defines the modular event structure.

schemas/earth-brain-lifecycle.schema.json
= Defines how an event moves through states and transitions.
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

* Added support for transition rules including:

```text
from_state
to_state
condition
requires_review
review_type
```

* Added support for transition history including:

```text
transition_id
timestamp
from_state
to_state
transition_actor
transition_reason
validation_result
review_reference
```

### Review Boundaries

* Added review boundary fields for:

```text
human_review_required
governance_review_required
defense_review_required
circulation_review_required
automatic_completion_allowed
```

* Established the principle that high-impact events should not silently complete without review.

### Terminal States

* Added terminal states:

```text
completed
archived
rejected
suspended
```

These terminal states end the active lifecycle flow while preserving lifecycle history.

### Validation

* Updated `scripts/validate_examples.py` to validate:

```text
examples/earth-brain-event.example.yaml
→ schemas/earth-brain-event.schema.json

examples/earth-brain-lifecycle.example.yaml
→ schemas/earth-brain-lifecycle.schema.json
```

* Maintained compatibility with the existing GitHub Actions workflow:

```text
.github/workflows/validate-examples.yml
```

### Documentation

* Added `docs/event-lifecycle-state-machine.md` to explain:

  * lifecycle purpose
  * state definitions
  * default transition flow
  * alternative review paths
  * transition rules
  * transition history
  * transition actors
  * review boundaries
  * terminal states
  * relationship to v0.2, v0.4, and v0.5

### Design Notes

* v0.3 does not require a new repository because it builds directly on the v0.2 modular architecture.
* v0.3 adds time, movement, and procedural memory to modular events.
* The lifecycle model is designed to remain compatible with future layer modules.

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
* Defined fields for:

  * layer identity
  * agent role
  * agent type
  * autonomy level
  * interaction scope
  * input channels
  * output channels
  * reasoning modes
  * trace requirements
  * governance constraints
  * human review boundary
  * operational status

### Validation

* Added local validation support using:

  * `jsonschema`
  * `pyyaml`

* Added GitHub Actions workflow to validate examples on:

  * push to `main`
  * pull requests to `main`
  * manual workflow dispatch

* Confirmed that the initial validation pipeline passes with the AI Agent Layer module.

### Design Notes

* v0.2 is maintained as a separate repository because the modular `$ref` architecture changes the structure of the system significantly from v0.1.
* The staged modular approach is intended to reduce schema coupling, improve validation stability, and allow new layers to be added one at a time.
* The first validated module is the AI Agent Layer, which serves as the routing and reasoning interface for future Earth Brain OS layers.

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

* human-to-AI event flow
* AI-to-governance feedback
* regulation and defense return paths

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
Version: v0.3.0-candidate
Architecture: Modular Event Architecture + Lifecycle State Machine
Current module: AI Agent Layer
Lifecycle model: Enabled
Validation: Passing
```

