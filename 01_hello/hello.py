#!/usr/bin/env python3
"""hello module."""

import argparse
from typing import Any


def get_args(args: list[Any] | None = None) -> argparse.Namespace:
    """Get parsed argparse agruments."""
    parser = argparse.ArgumentParser(
        description="Say hello",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-n",
        "--name",
        default="World",
        help="The name to greet",
    )

    return parser.parse_args(args)


def main():
    """Run main logic."""
    args = get_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
