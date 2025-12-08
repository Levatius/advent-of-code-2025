import pytest

from test.utils import get_aoc_imports

parse, part_1, part_2, puzzle_input_lines = get_aoc_imports()


@pytest.fixture
def example_1():
    return parse(
        [
            "162,817,812",
            "57,618,57",
            "906,360,560",
            "592,479,940",
            "352,342,300",
            "466,668,158",
            "542,29,236",
            "431,825,988",
            "739,650,466",
            "52,470,668",
            "216,146,977",
            "819,987,18",
            "117,168,530",
            "805,96,715",
            "346,949,466",
            "970,615,88",
            "941,993,340",
            "862,61,35",
            "984,92,344",
            "425,690,689",
        ]
    )


@pytest.fixture
def puzzle_input():
    return parse(puzzle_input_lines)


def test__part_1__example_1(example_1):
    assert part_1(example_1, connection_limit=10) == 40


def test__part_1__puzzle_input(puzzle_input):
    print(part_1(puzzle_input, connection_limit=1000))


def test__part_2__example_1(example_1):
    assert part_2(example_1) == 25272


def test__part_2__puzzle_input(puzzle_input):
    print(part_2(puzzle_input))
