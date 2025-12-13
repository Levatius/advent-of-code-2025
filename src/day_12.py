import math
import re
from dataclasses import dataclass
from itertools import batched

from shapely.geometry.polygon import Polygon
from shapely.ops import unary_union

TOTAL_PRESENT_TYPES = 6
PRESENT_BLOCK_SIZE = 5


@dataclass
class Region:
    size: tuple[int, int]
    present_counts: list[int]

    @classmethod
    def from_line(cls, line: str):
        size_str, present_counts_str = re.fullmatch(r"(.+): (.+)", line).groups()
        size_parts = size_str.split("x")
        size = int(size_parts[0]), int(size_parts[1])
        present_counts = list(map(int, present_counts_str.split()))
        return cls(size, present_counts)


def parse(lines: list[str]) -> tuple[list[Polygon], list[Region]]:
    presents = []
    for line_block in batched(lines[: PRESENT_BLOCK_SIZE * TOTAL_PRESENT_TYPES], n=PRESENT_BLOCK_SIZE):
        present_lines = line_block[1 : PRESENT_BLOCK_SIZE - 1]
        squares = []
        for j, line in enumerate(present_lines):
            for i, char in enumerate(line):
                if char == "#":
                    squares.append(Polygon([(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)]))
        presents.append(unary_union(squares).simplify(tolerance=0, preserve_topology=True))

    regions = [Region.from_line(line) for line in lines[PRESENT_BLOCK_SIZE * TOTAL_PRESENT_TYPES :]]

    return presents, regions


def part_1(presents: list[Polygon], regions: list[Region]) -> int:
    total = 0
    for region in regions:
        actual_presents_area = sum(
            presents[i].area * present_count for i, present_count in enumerate(region.present_counts)
        )
        # Skip if the presents cannot physically fit into the region
        if actual_presents_area > math.prod(region.size):
            continue
        simple_presents_area = sum(9 * present_count for present_count in region.present_counts)
        # Guaranteed solve if the 3x3 present grids can fit into the region (rounding the region bounds down)
        if simple_presents_area <= math.prod((length // 3) * 3 for length in region.size):
            total += 1
            continue
        # TODO: General solve would go here, but the puzzle input is fixed so that this is not reached
    return total


def part_2(presents: list[Polygon], regions: list[Region]) -> None:
    # There is no Part 2, Christmas is saved!
    return None
