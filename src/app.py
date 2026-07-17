#!/usr/bin/env python3
"""TechStart Team Directory — lists the profiles in profiles/.

Run:  python3 src/app.py
"""

import re
from pathlib import Path

PROFILES = Path(__file__).parent.parent / "profiles"


def read_profile(path):
    text = path.read_text(encoding="utf-8")
    name = re.search(r"^# (.+)$", text, re.MULTILINE)
    role = re.search(r"^- \*\*Role:\*\* (.+)$", text, re.MULTILINE)
    return {
        "name": name.group(1).strip() if name else "(no name)",
        "role": role.group(1).strip() if role else "(no role)",
    }


def main():
    files = [p for p in sorted(PROFILES.glob("*.md")) if not p.name.startswith("_")]

    print()
    print("  TechStart Team Directory")
    print("  " + "-" * 44)

    if not files:
        print("  Nobody has a profile yet.")
        print("  Copy profiles/_template.md and add yours!")
        print()
        return

    for f in files:
        p = read_profile(f)
        print(f"  {p['name']:<26} {p['role']}")

    print("  " + "-" * 44)
    print(f"  {len(files)} people on the team")
    print()


if __name__ == "__main__":
    print("Hello world")
    main()

