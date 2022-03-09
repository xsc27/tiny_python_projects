#!/usr/bin/env python3
"""picnic module."""

import argparse
from typing import Any


def get_args(args: list[Any] | None = None) -> argparse.Namespace:
    """Get parsed argparse agruments."""
    parser = argparse.ArgumentParser(
        description="Picnic game.",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "str",
        nargs="+",
        type=str,
        help="Item(s) to bring",
    )
    parser.add_argument(
        "-s",
        "--sorted",
        action="store_true",
        help="Sort the items",
    )

    parser.add_argument(
        "-x",
        "--no-oxford",
        action="store_false",
        help="Do not use Oxford comma",
    )

    parser.add_argument(
        "-c",
        "--separator",
        default=",",
        type=str,
        help="Separator",
    )

    return parser.parse_args(args)


def get_message(
    items: list[str], sort: bool = False, oxford: bool = True, separator: str = ","
) -> str:
    """Get message.

    >>> get_message(["chips", "pie", "soda"], separator=";")
    'You are bringing chips; pie; and soda.'
    >>> get_message(["chips", "pie", "soda"], oxford=False)
    'You are bringing chips, pie and soda.'
    >>> get_message([])
    Traceback (most recent call last):
    ValueError: Empty list.
    """
    if not items:
        raise ValueError("Empty list.")
    items.sort() if sort else items
    connect = f"{separator if oxford and len(items) > 2 else ''} and " if len(items) > 1 else ""
    return f"You are bringing {f'{separator} '.join(items[:-1])}{connect}{items[-1]}."


def main():
    """Run main logic."""
    args = get_args()
    print(
        get_message(args.str, sort=args.sorted, oxford=args.no_oxford, separator=args.separator)
    )


if __name__ == "__main__":
    main()
