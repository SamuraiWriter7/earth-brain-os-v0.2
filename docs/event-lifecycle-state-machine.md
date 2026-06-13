# Event Lifecycle State Machine

## Earth Brain OS v0.3

**Lifecycle State Machine for modular Earth Brain events.**

Earth Brain OS v0.3 extends the v0.2 Modular Event Architecture by adding lifecycle states, transition rules, review boundaries, and terminal states.

v0.2 separates the Earth Brain OS event into modular layers.
v0.3 defines how those events move through time.

```text
v0.2 = Modular Event Architecture
       Layer schemas are separated and referenced through $ref.

v0.3 = Lifecycle State Machine
       Events gain state, transition history, review boundaries, and completion paths.
```

In short:

> v0.2 gives Earth Brain OS its modular body.
> v0.3 gives it pulse, flow, and procedural memory.

---

## Purpose

The purpose of the lifecycle state machine is to make Earth Brain OS events:

* traceable
* reviewable
* governable
* suspendable
* archivable
* reusable as structured process records

Without lifecycle modeling, an event is only a static record.

With lifecycle modeling, an event becomes a process that can be validated, routed, reviewed, approved, completed, rejected, suspended, or archived.

---

## Core Files

v0.3 introduces the following files:

```text
schemas/earth-brain-lifecycle.schema.json
docs/event-lifecycle-state-machine.md
examples/earth-brain-lifecycle.example.yaml
```

The lifecycle schema validates lifecycle records linked to Earth Brain event records.

```text
earth_brain_event_id: "earth-brain-event-001"
```

This allows a lifecycle record to govern a specific event defined under:

```text
schemas/earth-brain-event.schema.json
```

---

## State Model

The lifecycle state machine defines the following states:

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

These states represent the major procedural phases of an Earth Brain OS event.

---

## State Definitions

### intake

The event has entered the system but has not yet been structured.

This is the raw entry point for an event, signal, prompt, trace, or system input.

---

### draft

The event has been structured into an initial record.

At this stage, the event may still be incomplete and should not be treated as validated.

---

### schema_validation

The event is checked against the relevant JSON Schema.

For v0.2 and v0.3, this includes validation through:

```text
scripts/validate_examples.py
```

---

### layer_routing

The event is routed to one or more relevant modular layers.

For the current implementation, the first validated layer is:

```text
schemas/layers/ai-agent-layer.schema.json
```

Future routing targets may include:

```text
schemas/layers/optical-nervous-layer.schema.json
schemas/layers/knowledge-cortex-layer.schema.json
schemas/layers/trace-attribution-layer.schema.json
schemas/layers/royalty-circulation-layer.schema.json
schemas/layers/kazene-regulation-layer.schema.json
schemas/layers/defense-immune-layer.schema.json
schemas/layers/human-governance-layer.schema.json
```

---

### layer_processing

The routed layer processes the event according to its role.

For the AI Agent Layer, this may include:

* interpretation
* reasoning
* routing
* assistant response generation
* human review request
* trace-aware decision support

---

### trace_check

The event is checked for traceability, attribution, and decision logging.

This state asks:

```text
Where did the input come from?
What action was performed?
Which layer processed it?
Is attribution required?
Is a decision log required?
```

Trace checking is essential for avoiding opaque AI action.

---

### human_review

The event requires human review.

This state is used when an event involves:

* high-impact decisions
* external actions
* uncertain reasoning
* governance change
* defense escalation
* royalty allocation change
* user-requested review

The human review boundary ensures that AI agents do not silently finalize high-impact transitions.

---

### governance_review

The event requires governance-level review.

This state is used when the event affects policy, institutional rules, permissions, rights, or structural governance conditions.

---

### defense_review

The event requires defense or immune-system review.

This state is used when the event may involve:

* adversarial input
* prompt injection
* manipulation
* security risk
* abnormal routing
* defensive escalation

---

### circulation_review

The event requires review related to value circulation, royalty routing, allocation, or return paths.

This state connects lifecycle governance with future royalty circulation layers.

---

### approved

The event has passed the required review conditions.

Approval does not necessarily mean completion.
It means the event is authorized to proceed toward finalization.

---

### completed

The event has finished its active lifecycle.

A completed event may still be archived, referenced, or used as a prior trace record.

---

### archived

The event has been stored for future reference.

Archived events are no longer active but remain part of the procedural memory of the system.

---

### rejected

The event has been reviewed and rejected.

Rejected events should retain their transition history and rejection reason.

---

### suspended

The event has been paused due to unresolved risk, uncertainty, governance conflict, or defense concern.

A suspended event is not deleted.
It remains available for future review.

---

## Default Transition Flow

The basic lifecycle flow is:

```text
intake
  ↓
draft
  ↓
schema_validation
  ↓
layer_routing
  ↓
layer_processing
  ↓
trace_check
  ↓
human_review
  ↓
approved
  ↓
completed
  ↓
archived
```

This is the standard positive path.

---

## Alternative Paths

Lifecycle flows may branch when review conditions fail or risk is detected.

### Rejection Path

```text
human_review
  ↓
rejected
```

### Defense Suspension Path

```text
defense_review
  ↓
suspended
```

### Governance Review Path

```text
trace_check
  ↓
governance_review
  ↓
approved
```

### Circulation Review Path

```text
trace_check
  ↓
circulation_review
  ↓
approved
```

These paths allow the system to avoid forcing every event into a single completion route.

---

## Transition Rules

Transition rules are defined in:

```text
schemas/earth-brain-lifecycle.schema.json
```

Each transition rule includes:

```yaml
from_state: "draft"
to_state: "schema_validation"
condition: "Draft event is ready for schema validation."
requires_review: false
review_type: "none"
```

A transition rule describes what movement is allowed and under what condition.

---

## Transition History

Each lifecycle record includes a transition history.

Example:

```yaml
transition_history:
  - transition_id: "transition-001"
    timestamp: "2026-06-13T00:00:00Z"
    from_state: "intake"
    to_state: "draft"
    transition_actor: "system"
    transition_reason: "Initial lifecycle record created for the Earth Brain event."
    validation_result: "not_applicable"
```

Transition history is the procedural memory of the event.

It records not only the current state, but how the event arrived there.

---

## Transition Actors

The lifecycle schema supports the following transition actors:

```text
human_operator
ai_agent_layer
validation_script
governance_reviewer
defense_reviewer
circulation_reviewer
system
```

This allows the lifecycle record to distinguish between automated transitions, AI-assisted transitions, human-reviewed transitions, and governance or defense decisions.

---

## Review Boundaries

Review boundaries define whether human or institutional review is required before certain transitions.

The schema supports:

```yaml
review_boundaries:
  human_review_required: true
  governance_review_required: false
  defense_review_required: false
  circulation_review_required: false
  automatic_completion_allowed: false
```

The key principle is:

> High-impact events should not silently complete without review.

This does not mean every event requires heavy governance.
It means the lifecycle must clearly express when review is required and when automatic completion is allowed.

---

## Terminal States

Terminal states end the active lifecycle flow.

```text
completed
archived
rejected
suspended
```

A terminal state does not mean the record disappears.

It means the event is no longer actively moving through the standard lifecycle.

---

## Relationship to v0.2

v0.2 defines the modular body of Earth Brain OS:

```text
schemas/earth-brain-event.schema.json
└─ layers.ai_agent_layer
   └─ $ref: ./layers/ai-agent-layer.schema.json
```

v0.3 defines how events move through that body:

```text
intake → draft → validation → routing → processing → review → completion
```

Together:

```text
v0.2 = What layers exist?
v0.3 = How does an event move through them?
```

---

## Relationship to Future Versions

### v0.4 — Bidirectional Event Flow

v0.4 may define directional flows between human, AI, trace, circulation, regulation, defense, and governance layers.

Example:

```text
human → AI → trace → circulation → governance
governance → regulation → defense → AI → human
```

### v0.5 — Event Processing Pipeline

v0.5 may define an operational processing sequence.

Example:

```text
intake → validation → routing → trace → review → circulation → archive
```

v0.3 is the bridge between static modular schemas and future event processing pipelines.

---

## Minimal Lifecycle Example

A minimal lifecycle record is provided in:

```text
examples/earth-brain-lifecycle.example.yaml
```

It validates against:

```text
schemas/earth-brain-lifecycle.schema.json
```

Run validation:

```bash
python scripts/validate_examples.py
```

---

## Design Principles

### 1. Events should have memory

An event should not only contain data.
It should remember its movement through the system.

---

### 2. Review should be explicit

If a transition requires human, governance, defense, or circulation review, that requirement should be visible in the lifecycle record.

---

### 3. Suspension is safer than silent failure

High-risk events should be suspendable instead of being deleted, ignored, or forced into completion.

---

### 4. Completion should not erase trace

Completed events should remain traceable and archivable.

---

### 5. Lifecycle should remain modular

The lifecycle model should work with current and future layer schemas without becoming a monolithic process engine.

---

## Summary

Earth Brain OS v0.3 introduces a lifecycle state machine for modular Earth Brain events.

It allows events to move through structured states such as intake, validation, routing, processing, trace checking, human review, approval, completion, rejection, suspension, and archival.

This turns Earth Brain OS from a static event model into a procedural architecture.

The event now has a path.

The path now has memory.

The memory now has review boundaries.
