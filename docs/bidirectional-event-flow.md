# Bidirectional Event Flow

## Earth Brain OS v0.4

**Bidirectional Event Flow for modular Earth Brain OS events.**

Earth Brain OS v0.4 extends the v0.3 Lifecycle State Machine by defining how events move forward and return across modular layers.

v0.2 separated the Earth Brain OS into modular schemas.
v0.3 gave events lifecycle states and transition memory.
v0.4 defines bidirectional flow between human, AI, trace, defense, circulation, regulation, and governance layers.

```text
v0.2 = Modular Event Architecture
       Layer schemas are separated and referenced through $ref.

v0.3 = Lifecycle State Machine
       Events gain states, transition rules, transition history,
       review boundaries, and terminal states.

v0.4 = Bidirectional Event Flow
       Events move forward and return across layers through feedback,
       review, defense, trace, and governance paths.
```

In short:

```text
v0.2 = What layers exist?
v0.3 = How does an event move through states?
v0.4 = How do layers send events forward and return signals back?
```

---

## Purpose

The purpose of Bidirectional Event Flow is to prevent Earth Brain OS events from becoming one-way commands.

A one-way event flow looks like this:

```text
human → AI → output
```

This is simple, but fragile.

A bidirectional event flow looks like this:

```text
human → AI → trace → review → governance
governance / defense / trace / human feedback → AI → human
```

This allows the system to:

* return feedback
* request clarification
* correct reasoning
* suspend risky flows
* require human review
* preserve trace records
* route governance or defense signals back into the event path

The key principle is:

> An event should not only move forward.
> It should also know how to return.

---

## Core Files

v0.4 introduces the following files:

```text
schemas/earth-brain-bidirectional-flow.schema.json
docs/bidirectional-event-flow.md
examples/earth-brain-bidirectional-flow.example.yaml
```

The bidirectional flow schema validates flow records linked to:

```text
schemas/earth-brain-event.schema.json
schemas/earth-brain-lifecycle.schema.json
```

A bidirectional flow record references both:

```yaml
earth_brain_event_id: "earth-brain-event-001"
lifecycle_id: "earth-brain-lifecycle-001"
```

This connects event structure, lifecycle state, and layer-to-layer flow.

---

## Flow Model

The canonical model name is:

```text
Earth Brain Bidirectional Event Flow
```

The model defines:

* participating layers
* directed flow edges
* return paths
* review boundaries
* active direction
* flow summary
* operational status

---

## Participating Layers

A bidirectional flow may involve the following layers:

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

The current minimal v0.4 example uses:

```text
human_governance_layer
ai_agent_layer
trace_attribution_layer
defense_immune_layer
```

This is enough to express the first complete forward-and-return loop.

---

## Active Direction

The schema supports four active direction states:

```text
forward
return
feedback_loop
suspended
```

### forward

The event is moving outward through the system.

Example:

```text
human_governance_layer → ai_agent_layer → trace_attribution_layer
```

### return

The event is moving back toward a prior layer.

Example:

```text
human_governance_layer → ai_agent_layer
```

### feedback_loop

The event is moving through an iterative loop.

Example:

```text
human → AI → trace → human review → AI refinement → human
```

### suspended

The flow is paused due to risk, uncertainty, review failure, or defense intervention.

---

## Forward Flow

The default forward path is:

```text
human_governance_layer
  ↓
ai_agent_layer
  ↓
trace_attribution_layer
  ↓
human_governance_layer
```

This means:

1. A human operator submits intent.
2. The AI Agent Layer interprets or reasons over the event.
3. The event is connected to trace attribution.
4. The trace result triggers review or completion.

Forward flow is not blind execution.
It remains trace-aware and review-aware.

---

## Return Flow

Return flow sends signals back to earlier layers.

Examples:

```text
human_governance_layer → ai_agent_layer
trace_attribution_layer → ai_agent_layer
defense_immune_layer → ai_agent_layer
kazene_regulation_layer → ai_agent_layer
governance_layer → human_governance_layer
```

Return flow may carry:

* clarification requests
* correction signals
* source attribution requests
* defense alerts
* governance constraints
* circulation feedback
* suspension notices

This is where the system becomes adaptive.

---

## Feedback Loop

A full feedback loop may look like this:

```text
human_governance_layer
  ↓
ai_agent_layer
  ↓
trace_attribution_layer
  ↓
human_governance_layer
  ↓
ai_agent_layer
  ↓
human_governance_layer
```

This loop allows a human reviewer to send clarification or correction back to the AI Agent Layer.

The AI Agent Layer can then refine its reasoning, update trace records, or request further review.

The loop should not continue endlessly.
Future versions may define loop limits, retry counts, or escalation paths.

---

## Defense Interruption

The Defense Immune Layer may interrupt the flow when risk is detected.

Example:

```text
defense_immune_layer
  ↓
ai_agent_layer
```

This may occur when the event contains:

* adversarial input
* prompt injection risk
* manipulation attempts
* unsafe routing
* uncertain reasoning
* abnormal event behavior

The defense layer does not merely block.
It can return a safer routing signal.

```text
risk detected → constrained reasoning → human review
```

This makes defense part of the circulatory system, not just a wall.

---

## Trace Feedback

The Trace Attribution Layer may return a signal to the AI Agent Layer when attribution is incomplete.

Example:

```text
trace_attribution_layer
  ↓
ai_agent_layer
```

This return path may request:

* source references
* decision logs
* attribution metadata
* origin records
* confidence clarification

This prevents AI outputs from becoming detached from their origin.

---

## Human Feedback

The Human Governance Layer may return a signal to the AI Agent Layer.

Example:

```text
human_governance_layer
  ↓
ai_agent_layer
```

This may happen when a human reviewer:

* requests clarification
* rejects a proposed output
* asks for safer reasoning
* requires a narrower scope
* adds governance constraints
* changes the intended purpose

Human feedback is not outside the system.
It is part of the event flow.

---

## Flow Edges

Flow edges define directed movement between layers.

Example:

```yaml
flow_edges:
  - edge_id: "flow-edge-001"
    direction: "forward"
    source_layer: "human_governance_layer"
    target_layer: "ai_agent_layer"
    signal_type: "human_intent"
    condition: "A human operator submits an intent or question to the AI Agent Layer."
    trace_required: true
    review_required: false
    lifecycle_state_hint: "intake"
```

Each flow edge includes:

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

A flow edge is the smallest directional unit of the bidirectional architecture.

---

## Signal Types

The schema supports the following signal types:

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

Signal types make it clear what kind of event is moving through an edge.

For example:

```text
human_intent       = a human-originated instruction or question
trace_update       = a trace or attribution update
review_request     = a request for human or governance review
defense_signal     = a risk or immune-system signal
feedback_signal    = a correction, clarification, or return signal
suspension_signal  = a signal that pauses the flow
```

---

## Return Paths

Return paths define how feedback or review signals move back through the system.

Example:

```yaml
return_paths:
  - path_id: "return-path-001"
    return_type: "human_feedback"
    from_layer: "human_governance_layer"
    to_layer: "ai_agent_layer"
    trigger: "Human reviewer requests clarification from the AI Agent Layer."
    requires_human_attention: true
    trace_reference: "trace-record-001"
```

Each return path includes:

```text
path_id
return_type
from_layer
to_layer
trigger
requires_human_attention
trace_reference
```

Return paths are the main difference between a processing pipeline and a living event flow.

---

## Return Types

The schema supports these return types:

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

Each return type represents a different kind of corrective or regulatory signal.

---

## Review Boundaries

Bidirectional flow must remain review-aware.

The schema supports:

```yaml
review_boundaries:
  human_review_on_return_required: true
  governance_review_on_policy_change_required: true
  defense_review_on_risk_required: true
  trace_required_for_all_edges: true
  automatic_forward_flow_allowed: true
  automatic_return_flow_allowed: false
```

The important distinction is:

```text
forward flow may be automatic when validation passes
return flow may require review when it changes meaning, scope, risk, or governance
```

This prevents feedback loops from becoming hidden autonomous control loops.

---

## Relationship to Lifecycle States

Bidirectional flow is connected to lifecycle states through:

```yaml
lifecycle_state_hint: "human_review"
```

This allows a flow edge to indicate which lifecycle state it belongs to.

Example relationship:

```text
human_governance_layer → ai_agent_layer
signal_type: feedback_signal
lifecycle_state_hint: human_review
```

The lifecycle schema tracks where the event is.
The bidirectional flow schema tracks how the event moves between layers.

Together:

```text
Lifecycle = state over time
Flow      = movement between layers
```

---

## Relationship to v0.2

v0.2 defines the modular body:

```text
schemas/earth-brain-event.schema.json
└─ layers.ai_agent_layer
   └─ $ref: ./layers/ai-agent-layer.schema.json
```

v0.4 depends on this modular idea.

Without modular layers, bidirectional flow has no clear source and target.

```text
v0.2 = layer identity
v0.4 = movement between layer identities
```

---

## Relationship to v0.3

v0.3 defines lifecycle state:

```text
intake → draft → schema_validation → layer_routing → layer_processing → trace_check → human_review
```

v0.4 adds directional flow between layers during those states.

Example:

```text
lifecycle state: trace_check
flow edge: ai_agent_layer → trace_attribution_layer
```

Another example:

```text
lifecycle state: human_review
return path: human_governance_layer → ai_agent_layer
```

---

## Relationship to Future v0.5

v0.5 may define an Event Processing Pipeline.

Example:

```text
intake → validation → routing → trace → review → circulation → archive
```

v0.4 prepares the ground by defining the directional and return-flow structure.

```text
v0.3 = state machine
v0.4 = bidirectional movement
v0.5 = operational pipeline
```

---

## Minimal Example

A minimal bidirectional flow example is provided in:

```text
examples/earth-brain-bidirectional-flow.example.yaml
```

It validates against:

```text
schemas/earth-brain-bidirectional-flow.schema.json
```

Run validation:

```bash
python scripts/validate_examples.py
```

---

## Design Principles

### 1. No one-way civilization events

Civilizational event systems should not be modeled as simple one-way commands.

Every meaningful event should be able to return, correct, review, suspend, or clarify.

---

### 2. Feedback is part of governance

Feedback is not an afterthought.
It is a governance mechanism.

---

### 3. Defense should interrupt and redirect

Defense should not only block dangerous events.
It should be able to redirect events toward safer reasoning, review, or suspension.

---

### 4. Trace should follow every edge

If an event moves across layers, its path should remain traceable.

---

### 5. Human review should remain visible

Human review should not be hidden outside the architecture.
It should be modeled as a layer and as a return path.

---

### 6. Return flow should not become invisible automation

Automatic forward movement may be acceptable for low-risk validated events.
Automatic return movement should be constrained when it changes meaning, policy, risk, or decision scope.

---

## Summary

Earth Brain OS v0.4 introduces Bidirectional Event Flow.

It defines how events move forward through modular layers and how review, defense, trace, governance, regulation, circulation, and human feedback return through the system.

The result is not a one-way AI pipeline.

It is a circulatory architecture.

The event moves forward.
The trace returns.
The defense interrupts.
The human reviews.
The AI refines.
The system remembers.

That is the core of v0.4.
