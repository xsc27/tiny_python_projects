#!/usr/bin/env python3
"""wc module."""

import argparse
import sys
from io import TextIOWrapper
from typing import Sequence

TEMPLATE = "{:8} {:7} {:7} {}"


def get_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    """Get parsed argparse agruments."""
    parser = argparse.ArgumentParser(
        description="Emulate wc (word count)",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "files",
        nargs="*",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
        help="Input file(s)",
    )

    return parser.parse_args(args)


def count(fid: TextIOWrapper) -> tuple[int, int, int]:
    """Count the charaters, letters, and lines in a file."""
    chars, words, lines = 0, 0, 0
    for line in fid:
        lines += 1
        words += len(line.split())
        chars += len(line)
    return lines, words, chars


def main(args: Sequence[str] | None = None):
    """Run main logic."""
    parsed_args = get_args(args)

    sums = {fid.name: count(fid) for fid in parsed_args.files}

    for file, values in sums.items():
        print(TEMPLATE.format(*values, file))
    if len(parsed_args.files) > 1:
        print(TEMPLATE.format(*list(map(sum, zip(*sums.values()))), "total"))


if __name__ == "__main__":
    main()
