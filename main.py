"""Write one short text to an output folder for the make.fun bounty."""

import os
import sys
from pathlib import Path

TEXT = (
    "My agent's dry run passed. Its wet run deleted the branch, "
    "because dry was not in the schema."
)


def output_dir() -> Path:
    """Return the folder to write into: MAKEFUN_OUTPUT_DIR, then OUTPUT_DIR, else /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        configured = os.environ.get(name)
        if configured:
            return Path(configured)
    return Path("/output")


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"

    folder = output_dir()
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
