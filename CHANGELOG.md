# Changelog

All notable changes to this project will be documented in this file.

This repository follows a candidate-based release flow for schema and reference model development.

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

### Planned

Future v0.2 layer modules:

```text
schemas/layers/optical-nervous-layer.schema.json
schemas/layers/knowledge-cortex-layer.schema.json
schemas/layers/trace-attribution-layer.schema.json
schemas/layers/royalty-circulation-layer.schema.json
schemas/layers/kazene-regulation-layer.schema.json
schemas/layers/defense-immune-layer.schema.json
schemas/layers/human-governance-layer.schema.json
```

Planned v0.3 direction:

```text
schemas/earth-brain-lifecycle.schema.json
docs/event-lifecycle-state-machine.md
examples/earth-brain-lifecycle.example.yaml
```

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
* transitions
* review and routing state changes

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
Version: v0.2.0-candidate
Architecture: Modular Event Architecture
Current module: AI Agent Layer
Validation: Passing
```
