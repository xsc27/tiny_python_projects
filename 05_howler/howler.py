#!/usr/bin/env python3
"""howler module."""

import argparse
import sys
from pathlib import Path
from typing import Sequence


def get_args(args: Sequence[str] | None = None) -> argparse.Namespace:
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
    """Get text from file or pass thru.

    >>> get_text("not a file")
    'not a file'
    """
    path = Path(text)
    return path.read_text() if path.is_file() else text


def change_case(text: str, lower: bool = False) -> str:
    """Change text to upper or lower case.

    >>> change_case("sOmE tExT")
    'SOME TEXT'
    >>> change_case("sOmE tExT", lower = True)
    'some text'
    """
    return getattr(get_text(text), "lower" if lower else "upper")()


def main(args: Sequence[str] | None = None):
    """Run main logic."""
    parsed_args = get_args(args)
    # print('some text', end='')
    with Path(parsed_args.outfile).open(mode="w") if parsed_args.outfile else sys.stdout as fid:
        print(change_case(parsed_args.text, parsed_args.ee), file=fid)


if __name__ == "__main__":
    main()


def test_get_text_file():
    """Verify when arg is a file, then the text of the file is returned."""
    ### Arrange
    arg = __file__
    expected = Path(arg).read_text()
    ### Act
    result = get_text(arg)
    ### Assert
    assert result == expected


def test_main_lower():
    ### Arrange
    results_file = Path("test_output.txt")
    args = ["-o", str(results_file), "--ee", "sOmE tExT"]
    expected = "some text\n"
    ### Act
    main(args)
    ### Assert
    assert results_file.read_text() == expected
    ### Cleanup
    results_file.unlink()
