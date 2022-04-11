#!/usr/bin/env python3
"""gashlycrumb module."""

import argparse
from typing import Sequence

DEFAULT_FILE = "gashlycrumb.txt"


def get_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    """Get parsed argparse agruments."""
    parser = argparse.ArgumentParser(
        description="Gashlycrumb",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "letter",
        nargs="+",
        type=str,
        help="Letter(s)",
    )
    parser.add_argument(
        "-f",
        "--file",
        type=argparse.FileType("rt"),
        default=DEFAULT_FILE,
        help="Input file",
    )

    return parser.parse_args(args)


def main(args: Sequence[str] | None = None):
    """Run main logic."""
    parsed_args = get_args(args)
    key_line = {line.split(" ", 1)[0].casefold(): line.strip() for line in parsed_args.file}
    output = [
        key_line.get(key.casefold(), f'I do not know "{key}".') for key in parsed_args.letter
    ]
    print("\n".join(output))


if __name__ == "__main__":
    main()
