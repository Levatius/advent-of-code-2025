from itertools import combinations

from shapely.geometry import Polygon


def parse(lines: list[str]) -> list[tuple]:
    return [tuple(map(int, line.split(","))) for line in lines]


def calculate_area(a: tuple, b: tuple) -> int:
    return int((abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1))


def part_1(red_tiles: list[tuple]) -> int:
    red_tile_pairs = sorted(combinations(red_tiles, 2), key=lambda pair: calculate_area(*pair), reverse=True)
    return calculate_area(*red_tile_pairs[0])


def part_2(red_tiles: list[tuple]) -> int:
    red_tile_polygon = Polygon(red_tiles)
    red_tile_pairs = sorted(combinations(red_tiles, 2), key=lambda pair: calculate_area(*pair), reverse=True)
    for a, b in red_tile_pairs:
        rectangle = Polygon([a, (a[0], b[1]), b, (b[0], a[1])])
        if rectangle.within(red_tile_polygon):
            return calculate_area(a, b)
    return 0
