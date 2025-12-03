import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1():
    return parse(
        [
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
        ]
    )


@pytest.fixture
def puzzle_input():
    return parse(puzzle_input_lines)


def test__part_1__example_1(example_1):
    assert part_1(example_1) == 1227775554


def test__part_1__puzzle_input(puzzle_input):
    print(part_1(puzzle_input))


def test__part_2__example_1(example_1):
    assert part_2(example_1) == 4174379265


def test__part_2__puzzle_input(puzzle_input):
    print(part_2(puzzle_input))
