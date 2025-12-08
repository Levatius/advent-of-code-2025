import math
from itertools import combinations

from networkx.utils import UnionFind


def parse(lines: list[str]) -> UnionFind:
    junctions = UnionFind(tuple(map(int, line.split(","))) for line in lines)
    return junctions


def part_1(junctions: UnionFind, connection_limit: int, circuit_limit: int = 3) -> int:
    junction_pairs = sorted(combinations(junctions, 2), key=lambda pair: math.dist(pair[0], pair[1]))
    for junction_a, junction_b in junction_pairs[:connection_limit]:
        junctions.union(junction_a, junction_b)
    circuit_sizes = sorted(junctions.weights.values(), reverse=True)
    return math.prod(circuit_sizes[:circuit_limit])


def part_2(junctions: UnionFind) -> int | None:
    junction_pairs = sorted(combinations(junctions, 2), key=lambda pair: math.dist(pair[0], pair[1]))
    for junction_a, junction_b in junction_pairs:
        junctions.union(junction_a, junction_b)
        # Check if any group in the UnionFind has all the junctions
        if any(weight == len(junctions.parents) for weight in junctions.weights.values()):
            return junction_a[0] * junction_b[0]
    return None
