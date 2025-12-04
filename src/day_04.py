ADJACENT_DIRECTIONS = [1 + 0j, 1 + 1j, 0 + 1j, -1 + 1j, -1 + 0j, -1 - 1j, 0 - 1j, 1 - 1j]
FORKLIFT_ACCESS_LIMIT = 4


def parse(lines: list[str]) -> set[complex]:
    rolls = set()
    for b, line in enumerate(lines):
        for a, char in enumerate(line):
            if char == "@":
                rolls.add(complex(a, b))
    return rolls


def part_1(rolls: set[complex]) -> int:
    total = 0
    for roll in rolls:
        adjacent_positions = (roll + direction for direction in ADJACENT_DIRECTIONS)
        if sum((adjacent in rolls) for adjacent in adjacent_positions) < FORKLIFT_ACCESS_LIMIT:
            total += 1
    return total


def part_2(rolls: set[complex]) -> int:
    total = 0
    while rolls:
        rolls_to_remove = set()
        for roll in rolls:
            adjacent_positions = (roll + direction for direction in ADJACENT_DIRECTIONS)
            if sum((adjacent in rolls) for adjacent in adjacent_positions) < FORKLIFT_ACCESS_LIMIT:
                total += 1
                rolls_to_remove.add(roll)
        if not rolls_to_remove:
            break
        rolls -= rolls_to_remove
    return total
