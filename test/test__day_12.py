import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1():
    return parse(
        [
            "0:",
            "###",
            "##.",
            "##.",
            "",
            "1:",
            "###",
            "##.",
            ".##",
            "",
            "2:",
            ".##",
            "###",
            "##.",
            "",
            "3:",
            "##.",
            "###",
            "##.",
            "",
            "4:",
            "###",
            "#..",
            "###",
            "",
            "5:",
            "###",
            ".#.",
            "###",
            "",
            "4x4: 0 0 0 0 2 0",
            "12x5: 1 0 1 0 2 2",
            "12x5: 1 0 1 0 3 2",
        ]
    )


@pytest.fixture
def puzzle_input():
    return parse(puzzle_input_lines)


@pytest.mark.skip(reason="General solution required, not implemented")
def test__part_1__example_1(example_1):
    assert part_1(*example_1) == 2


def test__part_1__puzzle_input(puzzle_input):
    print(part_1(*puzzle_input))


def test__part_2__puzzle_input():
    print(part_2())
