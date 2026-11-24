#!/usr/bin/env python3
"""Copy excuse.txt into <MAKEFUN_OUTPUT_DIR>/entry.txt."""

import os
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "excuse.txt"
ENTRY_NAME = "entry.txt"


def fail(message: str) -> int:
    """Print an error to stderr and return the failure exit code."""
    print(f"error: {message}", file=sys.stderr)
    return 1


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "./output"))
    dest = out_dir / ENTRY_NAME

    if not SOURCE.is_file():
        return fail(f"source not found: {SOURCE}")

    text = SOURCE.read_text(encoding="utf-8").strip()
    if not text:
        return fail(f"source is empty: {SOURCE}")

    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        dest.write_text(text + "\n", encoding="utf-8")
    except OSError as exc:
        return fail(f"cannot write {dest}: {exc}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
