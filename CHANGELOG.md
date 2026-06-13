# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-based release flow for schema and reference model development.

---

## [v0.5.0-candidate] - 2026-06-13

### Added

* Introduced **Event Processing Pipeline** as the core design direction for v0.5.
* Added processing pipeline schema:

```text
schemas/earth-brain-processing-pipeline.schema.json
```

* Added processing pipeline example:

```text
examples/earth-brain-processing-pipeline.example.yaml
```

* Added processing pipeline documentation:

```text
docs/event-processing-pipeline.md
```

* Updated validation script to include processing pipeline example validation:

```text
scripts/validate_examples.py
```

* Updated README to reflect v0.5 architecture, processing pipeline schema, documentation, examples, validation targets, design principles, and roadmap.

### Architecture

* Extended v0.4 Bidirectional Event Flow with an operational event processing sequence.

```text
v0.2 = Modular Event Architecture
       Layer schemas are separated and referenced through $ref.

v0.3 = Lifecycle State Machine
       Events gain states, transition rules, transition history,
       review boundaries, and terminal states.

v0.4 = Bidirectional Event Flow
       Events move forward and return across layers through feedback,
       trace, review, defense, governance, and human correction paths.

v0.5 = Event Processing Pipeline
       Events move through an operational sequence:
       intake → validation → routing → processing → trace → review → completion → archive.
```

* Defined the processing pipeline schema as the operational companion to the event, lifecycle, and bidirectional flow schemas.

```text
schemas/earth-brain-event.schema.json
= Defines the modular event structure.

schemas/earth-brain-lifecycle.schema.json
= Defines how an event moves through states and transitions.

schemas/earth-brain-bidirectional-flow.schema.json
= Defines how an event moves forward and returns across layers.

schemas/earth-brain-processing-pipeline.schema.json
= Defines how an event is operationally processed from intake to archive.
```

### Pipeline Model

* Added canonical pipeline model:

```text
Earth Brain Event Processing Pipeline
```

* Added support for:

```text
pipeline_id
version
pipeline_model
earth_brain_event_id
lifecycle_id
flow_id
pipeline_purpose
processing_mode
pipeline_stages
stage_transitions
operational_controls
review_boundaries
pipeline_summary
status
```

### Processing Modes

* Added processing modes:

```text
manual
assisted
semi_automated
bounded_automated
suspended
```

### Pipeline Stages

* Added supported pipeline stages:

```text
intake
schema_validation
layer_routing
layer_processing
trace_check
human_review
governance_review
defense_review
circulation_review
approval
completion
archive
suspension
```

* Established the minimal canonical path:

```text
intake
→ schema_validation
→ layer_routing
→ layer_processing
→ trace_check
→ human_review
→ approval
→ completion
→ archive
```

### Stage Fields

* Added stage-level fields:

```text
stage_id
stage_name
stage_order
stage_type
responsible_layer
input_signal
output_signal
required_state
completion_condition
trace_required
review_required
failure_action
notes
```

### Stage Transitions

* Added stage transition modeling with:

```text
transition_id
from_stage
to_stage
condition
on_failure
lifecycle_state_change
```

* Added support for pipeline transitions such as:

```text
intake → schema_validation
schema_validation → layer_routing
layer_routing → layer_processing
layer_processing → trace_check
trace_check → human_review
human_review → approval
approval → completion
completion → archive
layer_processing → defense_review
defense_review → suspension
```

### Failure Paths

* Added supported failure actions:

```text
retry
return_to_previous_stage
request_human_review
route_to_defense_review
suspend_pipeline
reject_event
archive_with_warning
```

### Operational Controls

* Added operational controls:

```text
max_retry_count
allow_manual_override
allow_pipeline_suspension
require_trace_before_completion
automatic_archive_allowed
```

### Review Boundaries

* Added pipeline-level review boundary fields:

```text
human_review_required_for_high_impact
governance_review_required_for_policy_change
defense_review_required_for_risk
circulation_review_required_for_value_flow
automatic_completion_allowed
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

examples/earth-brain-processing-pipeline.example.yaml
→ schemas/earth-brain-processing-pipeline.schema.json
```

* Maintained compatibility with the existing GitHub Actions workflow:

```text
.github/workflows/validate-examples.yml
```

### Documentation

* Added `docs/event-processing-pipeline.md` to explain:

  * purpose of the Event Processing Pipeline
  * pipeline model
  * processing modes
  * canonical pipeline
  * stage definitions
  * optional review stages
  * stage transitions
  * failure paths
  * defense path
  * suspension path
  * rejection path
  * operational controls
  * review boundaries
  * relationship to v0.2, v0.3, v0.4, and future versions

### Design Notes

* v0.5 does not require a new repository because it builds directly on the v0.2 modular architecture, v0.3 lifecycle model, and v0.4 bidirectional flow model.
* v0.5 turns Earth Brain OS from a bidirectional event flow model into an operational processing architecture.
* The pipeline is designed to be explicit, trace-aware, review-aware, suspendable, and archivable.
* Archive is treated as procedural memory, not disposal.
* Defense is modeled as a pipeline path, not an external exception.
* Completion is constrained by trace and review boundaries.

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

* Updated validation script to include bidirectional flow example validation.

### Architecture

* Extended v0.3 Lifecycle State Machine with bidirectional layer-to-layer event movement.

```text
v0.4 = Bidirectional Event Flow
       Events move forward and return across layers through feedback,
       trace, review, defense, governance, and human correction paths.
```

### Design Notes

* Return paths are treated as first-class schema objects.
* Defense is modeled as an interrupt-and-redirect layer.
* Human feedback is modeled as part of the system flow.

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

* Updated validation script to include lifecycle example validation.

### Architecture

* Extended v0.2 Modular Event Architecture with lifecycle modeling.

```text
v0.3 = Lifecycle State Machine
       Events gain states, transition rules, transition history,
       review boundaries, and terminal states.
```

### Design Notes

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

* operational pipeline stages
* stage transitions
* processing modes
* operational controls
* review boundaries
* failure paths
* archive as procedural memory

### v0.6

**Multi-Layer Expansion**

Planned focus:

* optical nervous layer
* knowledge cortex layer
* trace attribution layer
* royalty circulation layer
* Kazene regulation layer
* defense immune layer
* human governance layer

---

## Repository Status

```text
Version: v0.5.0-candidate
Architecture: Modular Event Architecture + Lifecycle State Machine + Bidirectional Event Flow + Event Processing Pipeline
Current module: AI Agent Layer
Lifecycle model: Enabled
Bidirectional flow model: Enabled
Processing pipeline model: Enabled
Validation: Passing
```

