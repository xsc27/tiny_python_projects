#!/usr/bin/env python3
"""crowsnet module."""

import argparse
from typing import Any, Literal


def get_args(args: list[Any] | None = None) -> argparse.Namespace:
    """Get parsed argparse agruments."""
    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        allow_abbrev=False,
    )
    parser.add_argument(
        "str",
        help="A word",
    )

    return parser.parse_args(args)


def get_article(word: str) -> Literal["a", "an"]:
    """Return article 'an' if word begins with a vowel, otherwise return 'a'.

    >>> get_article("consonants")
    'a'
    >>> get_article("apple")
    'an'
    >>> word="example"
    >>> f"This is {get_article(word)} {word}."
    'This is an example.'
    """
    return "an" if word.casefold().startswith(("a", "e", "i", "o", "u")) else "a"


def main():
    """Run main logic."""
    args = get_args()
    print(f"Ahoy, Captain, {get_article(args.str)} {args.str} off the larboard bow!")


if __name__ == "__main__":
    main()
