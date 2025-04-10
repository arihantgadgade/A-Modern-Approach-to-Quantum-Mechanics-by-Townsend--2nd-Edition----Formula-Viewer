#!/usr/bin/env python3
"""
rename_screenshots.py
Rename files that start with “Screenshot ” into sequential names such as 1_1.png, 1_2.png …

Usage
-----
    python3 rename_screenshots.py <prefix> [start_index]

    • <prefix>       text that goes in front of every new name (default: 1_)
    • [start_index]  first number to use           (default: 1)

Examples
--------
    python3 rename_screenshots.py 1_        # → 1_1.png, 1_2.png, …
    python3 rename_screenshots.py shot_ 10  # → shot_10.png, shot_11.png, …
"""
import sys, glob, os
from pathlib import Path

def main():
    prefix = sys.argv[1] if len(sys.argv) > 1 else "1_"
    start  = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    # macOS screenshots look like “Screenshot 2025‑04‑08 at 1.59.58 PM.png”
    files = glob.glob("Screenshot *")

    # Sort by creation (“birth”) time so numbering follows the moment you shot them
    files.sort(key=lambda f: Path(f).stat().st_birthtime)

    for idx, old in enumerate(files, start):
        old_p = Path(old)
        new_p = f"{prefix}{idx}{old_p.suffix}"
        print(f"{old}  ➜  {new_p}")
        old_p.rename(new_p)

if __name__ == "__main__":
    main()
