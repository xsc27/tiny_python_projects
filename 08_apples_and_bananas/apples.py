#!/usr/bin/env python3
"""Apples and Bananas"""

import argparse

# from concurrent.futures import ProcessPoolExecutor
from ctypes.wintypes import MAX_PATH
from pathlib import Path
from typing import Sequence

VOWELS = "aeiou"


def get_args(args: Sequence[str] | None = None) -> argparse.Namespace:
    """Get parsed argparse agruments."""

    parser = argparse.ArgumentParser(
        description="Apples and bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", help="Input text or file")

    parser.add_argument(
        "-v",
        "--vowel",
        help="The vowel to substitute",
        type=str,
        default="a",
        choices=list(VOWELS),
    )

    parsed_args = parser.parse_args(args)

    if len(parsed_args.text) <= MAX_PATH:
        path = Path(parsed_args.text)
        if path.is_file():
            parsed_args.text = path.read_text()

    return parsed_args


def solution_loop(args: Sequence[str] | None = None) -> str:
    """Iterate over text."""

    VOWELS_UPPER = VOWELS.upper()

    def swap_vowel(char: str) -> str:
        if char in VOWELS:
            return vowel
        if char in VOWELS_UPPER:
            return vowel.upper()
        return char

    ns_args = get_args(args)
    vowel = ns_args.vowel

    text = (swap_vowel(char) for char in ns_args.text)
    return "".join(text)


def solution_translate(args: Sequence[str] | None = None) -> str:
    """Use translate."""
    ns_args = get_args(args)
    vowel = ns_args.vowel
    trans = str.maketrans(VOWELS + VOWELS.upper(), vowel * 5 + vowel.upper() * 5)
    return ns_args.text.translate(trans)


def solution_replace(args: Sequence[str] | None = None) -> str:
    """Use replace."""
    ns_args = get_args(args)
    text = ns_args.text
    vowel = ns_args.vowel

    for v in VOWELS:
        text = text.replace(v, vowel).replace(v.upper(), vowel.upper())

    return text


def solution_map(args: Sequence[str] | None = None) -> str:
    """Iterate over text."""

    VOWELS_UPPER = VOWELS.upper()

    def swap_vowel(char: str) -> str:
        if char in VOWELS:
            return vowel
        if char in VOWELS_UPPER:
            return vowel.upper()
        return char

    ns_args = get_args(args)
    vowel = ns_args.vowel

    # with ProcessPoolExecutor() as executor:
    #     text = executor.map(
    #         swap_vowel, ns_args.text,
    #         chunksize= 10000,
    #     )
    text = map(swap_vowel, ns_args.text)

    return "".join(text)


IMPLEMENTATION = (
    solution_translate,
    solution_replace,
    solution_map,
    solution_loop,
)


def main(args: Sequence[str] | None = None, implementation: int = 0):
    """Run main logic."""

    print(IMPLEMENTATION[implementation](args))


if __name__ == "__main__":
    main()

# import cProfile
import gc
from time import time

import pytest


@pytest.mark.parametrize("i", range(4))
def test_profile(i: int):
    gc.disable()
    trys = 10
    size = 4 * 10**5
    text = Path("apples.py").read_text() * size
    func = IMPLEMENTATION[i]

    def run():
        gc.collect()
        start_time = time()
        func(args=[text])
        return time() - start_time

    print(
        f"{func.__name__} avg {sum(run() for _ in range(trys)) / float(trys)} secs "
        f"for {trys} executions on {text.__sizeof__()/float(1<<10):,.0f} KB."
    )

    # with cProfile.Profile() as pr:
    #     IMPLEMENTATION[i](args=[text])
    # pr.print_stats()
