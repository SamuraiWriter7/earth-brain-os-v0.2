#!/usr/bin/env python3
"""
Validate Earth Brain OS example files against JSON Schemas.

This validator is intentionally minimal and stable for GitHub Actions.

It currently validates:

* examples/earth-brain-event.example.yaml
  against
* schemas/earth-brain-event.schema.json

and:

* examples/earth-brain-lifecycle.example.yaml
  against
* schemas/earth-brain-lifecycle.schema.json

The integrated event schema may reference layer schemas via local $ref paths,
such as ./layers/ai-agent-layer.schema.json.
"""

from **future** import annotations

import json
import sys
import warnings
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker, RefResolver
from jsonschema.exceptions import ValidationError

# RefResolver is deprecated in newer jsonschema versions, but it remains

# useful and stable for simple local-file $ref validation in CI.

warnings.filterwarnings("ignore", category=DeprecationWarning)

REPO_ROOT = Path(**file**).resolve().parents[1]

VALIDATION_TARGETS = [
{
"example": REPO_ROOT / "examples" / "earth-brain-event.example.yaml",
"schema": REPO_ROOT / "schemas" / "earth-brain-event.schema.json",
},
{
"example": REPO_ROOT / "examples" / "earth-brain-lifecycle.example.yaml",
"schema": REPO_ROOT / "schemas" / "earth-brain-lifecycle.schema.json",
},
]

def load_json(path: Path) -> Any:
"""Load a JSON file."""
with path.open("r", encoding="utf-8") as file:
return json.load(file)

def load_yaml(path: Path) -> Any:
"""Load a YAML file."""
with path.open("r", encoding="utf-8") as file:
return yaml.safe_load(file)

def format_error(error: ValidationError) -> str:
"""Format a jsonschema validation error for readable CI output."""
location = ".".join(str(part) for part in error.absolute_path)
schema_location = " -> ".join(str(part) for part in error.absolute_schema_path)

```
if not location:
    location = "<root>"

return (
    f"Validation error at: {location}\n"
    f"Message: {error.message}\n"
    f"Schema path: {schema_location}"
)
```

def validate_file(example_path: Path, schema_path: Path) -> bool:
"""Validate one example file against one schema file."""
if not example_path.exists():
print(f"[ERROR] Example file not found: {example_path}")
return False

```
if not schema_path.exists():
    print(f"[ERROR] Schema file not found: {schema_path}")
    return False

print(f"[INFO] Validating {example_path.relative_to(REPO_ROOT)}")
print(f"[INFO] Using schema {schema_path.relative_to(REPO_ROOT)}")

schema = load_json(schema_path)
example = load_yaml(example_path)

resolver = RefResolver(
    base_uri=schema_path.as_uri(),
    referrer=schema,
)

validator = Draft202012Validator(
    schema,
    resolver=resolver,
    format_checker=FormatChecker(),
)

errors = sorted(
    validator.iter_errors(example),
    key=lambda error: list(error.absolute_path),
)

if errors:
    print(f"[FAIL] {example_path.relative_to(REPO_ROOT)}")
    for error in errors:
        print()
        print(format_error(error))
    return False

print(f"[PASS] {example_path.relative_to(REPO_ROOT)}")
return True
```

def main() -> int:
"""Run all configured validation targets."""
print("[INFO] Earth Brain OS example validation started.")

```
all_passed = True

for target in VALIDATION_TARGETS:
    passed = validate_file(
        example_path=target["example"],
        schema_path=target["schema"],
    )
    all_passed = all_passed and passed

if all_passed:
    print("[SUCCESS] All examples are valid.")
    return 0

print("[ERROR] One or more examples failed validation.")
return 1
```

if **name** == "**main**":
sys.exit(main())
