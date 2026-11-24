#!/usr/bin/env python3
"""Copy excuse.txt into <MAKEFUN_OUTPUT_DIR>/entry.txt."""

import os
import sys
from pathlib import Path


def main() -> int:
    src = Path(__file__).resolve().parent / "excuse.txt"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "./output"))

    if not src.is_file():
        print(f"error: source not found: {src}", file=sys.stderr)
        return 1

    text = src.read_text(encoding="utf-8").strip()
    if not text:
        print(f"error: source is empty: {src}", file=sys.stderr)
        return 1

    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_text(text + "\n", encoding="utf-8")
    except OSError as exc:
        print(f"error: cannot write entry: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
