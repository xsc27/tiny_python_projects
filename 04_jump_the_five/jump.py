#!/usr/bin/env python3
"""jump module."""

import argparse
from typing import Any

J0 = {
    "1": "9",
    "2": "8",
    "3": "7",
    "4": "6",
    "5": "0",
    "6": "4",
    "7": "3",
    "8": "2",
    "9": "1",
    "0": "5",
}
J1 = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero",
}
JUMPER = [J0, J1]


def get_args(args: list[Any] | None = None) -> argparse.Namespace:
    """Get parsed argparse agruments."""
    parser = argparse.ArgumentParser(
        description="Jump the Five",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "str",
        nargs="+",
        type=str,
        help="Input text",
    )

    return parser.parse_args(args)


def get_encoded(string: str, jumper: dict[str, Any] = JUMPER[0]) -> str:
    return "".join(jumper.get(c, "") if c.isnumeric() else c for c in string)


def main():
    """Run main logic."""
    args = get_args()
    print(get_encoded(" ".join(args.str)))


if __name__ == "__main__":
    main()

import random

import pytest


def test_round_trip():
    string = str(random.randint(10**9, 10**10))
    assert string == get_encoded(get_encoded(string))


@pytest.mark.parametrize(
    "string, expected",
    [
        ("509", "fivezeronine"),
        ("213-01", "twoonethree-zeroone"),
        ("this is 7.", "this is seven."),
    ],
)
def test_j1(string: str, expected: str):
    assert expected == get_encoded(string, JUMPER[1])
