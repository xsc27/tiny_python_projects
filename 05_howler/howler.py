#!/usr/bin/env python3
"""howler module."""

import argparse
import sys
from pathlib import Path
from typing import Any


def get_args(args: list[Any] | None = None) -> argparse.Namespace:
    """Get parsed argparse agruments."""
    parser = argparse.ArgumentParser(
        description="Howler (upper-cases input)",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-e",
        "--ee",
        action="store_true",
        help="lower-case instead",
    )
    parser.add_argument(
        "-o",
        "--outfile",
        metavar="str",
        default="",
        type=str,
        help="Output filename",
    )
    parser.add_argument(
        "text",
        type=str,
        help="Input string or file",
    )

    return parser.parse_args(args)


def get_text(text: str) -> str:
    """Get text from file or pass thru."""
    path = Path(text)
    return path.read_text() if path.is_file() else text


def change_case(text: str, lower: bool = False) -> str:
    """Change text to upper or lower case."""
    return getattr(get_text(text), "lower" if lower else "upper")()


def main():
    """Run main logic."""
    args = get_args()

    with Path(args.outfile).open(mode="w") if args.outfile else sys.stdout as fid:
        print(change_case(args.text, args.ee), file=fid)


if __name__ == "__main__":
    main()
