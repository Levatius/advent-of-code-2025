import re

ROTATION_DIRECTION_MAP = {"L": -1, "R": 1}
DIAL_START = 50
DIAL_SIZE = 100


def parse(lines: list[str]) -> list[int]:
    rotations = []
    for line in lines:
        direction, value_str = re.match(r"([LR])(\d+)", line).groups()
        value = int(value_str) * ROTATION_DIRECTION_MAP[direction]
        rotations.append(value)
    return rotations


def part_1(rotations: list[int]) -> int:
    total = 0
    dial_current = DIAL_START
    for rotation in rotations:
        if (dial_current := (dial_current + rotation) % DIAL_SIZE) == 0:
            total += 1
    return total


def part_2(rotations: list[int]) -> int:
    total = 0
    dial_current = DIAL_START
    for rotation in rotations:
        dial_virtual = (DIAL_SIZE - dial_current) % DIAL_SIZE if rotation < 0 else dial_current
        total += (dial_virtual + abs(rotation)) // DIAL_SIZE
        dial_current = (dial_current + rotation) % DIAL_SIZE
    return total
