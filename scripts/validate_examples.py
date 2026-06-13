#!/usr/bin/env python3
"""
Validate Earth Brain OS example files against JSON Schemas.
"""

from __future__ import annotations

import json
import sys
import warnings
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker, RefResolver
from jsonschema.exceptions import ValidationError

warnings.filterwarnings("ignore", category=DeprecationWarning)

REPO_ROOT = Path(__file__).resolve().parents[1]

VALIDATION_TARGETS = [
    {
        "example": REPO_ROOT / "examples" / "earth-brain-event.example.yaml",
        "schema": REPO_ROOT / "schemas" / "earth-brain-event.schema.json",
    },
    {
        "example": REPO_ROOT / "examples" / "earth-brain-lifecycle.example.yaml",
        "schema": REPO_ROOT / "schemas" / "earth-brain-lifecycle.schema.json",
    },
    {
        "example": REPO_ROOT / "examples" / "earth-brain-bidirectional-flow.example.yaml",
        "schema": REPO_ROOT / "schemas" / "earth-brain-bidirectional-flow.schema.json",
    },
    {
        "example": REPO_ROOT / "examples" / "earth-brain-processing-pipeline.example.yaml",
        "schema": REPO_ROOT / "schemas" / "earth-brain-processing-pipeline.schema.json",
    },
]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def format_error(error: ValidationError) -> str:
    location = ".".join(str(p) for p in error.absolute_path)
    schema_location = " -> ".join(str(p) for p in error.absolute_schema_path)

    if not location:
        location = "<root>"

    return (
        f"Validation error at: {location}\n"
        f"Message: {error.message}\n"
        f"Schema path: {schema_location}"
    )


def validate_file(example_path: Path, schema_path: Path) -> bool:
    if not example_path.exists():
        print(f"[ERROR] Example file not found: {example_path}")
        return False

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
        key=lambda e: list(e.absolute_path),
    )

    if errors:
        print(f"[FAIL] {example_path.relative_to(REPO_ROOT)}")
        for error in errors:
            print()
            print(format_error(error))
        return False

    print(f"[PASS] {example_path.relative_to(REPO_ROOT)}")
    return True


def main() -> int:
    print("[INFO] Earth Brain OS example validation started.")

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


if __name__ == "__main__":
    sys.exit(main())
