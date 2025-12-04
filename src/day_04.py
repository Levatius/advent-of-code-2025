import networkx as nx

EDGE_DIRECTIONS = [-1 + 0j, -1 - 1j, 0 - 1j, 1 - 1j]  # Only need a subset of the full 8 directions when building edges
FORKLIFT_ACCESS_LIMIT = 4


def parse(lines: list[str]) -> nx.Graph:
    rolls = nx.Graph()
    # Add rolls as nodes
    for b, line in enumerate(lines):
        for a, char in enumerate(line):
            if char == "@":
                rolls.add_node(complex(a, b))
    # Add edges between adjacent rolls
    for roll in rolls:
        for adjacent in [roll + direction for direction in EDGE_DIRECTIONS]:
            if adjacent in rolls:
                rolls.add_edge(roll, adjacent)
    return rolls


def part_1(rolls: nx.Graph) -> int:
    return len([roll for roll, adjacent_total in rolls.degree() if adjacent_total < FORKLIFT_ACCESS_LIMIT])


def part_2(rolls: nx.Graph) -> int:
    total = 0
    while rolls:
        movable_rolls = [roll for roll, adjacent_total in rolls.degree() if adjacent_total < FORKLIFT_ACCESS_LIMIT]
        if not movable_rolls:
            break
        total += len(movable_rolls)
        rolls.remove_nodes_from(movable_rolls)
    return total
