import re
from collections import defaultdict


def parse(lines: list[str]) -> tuple[list[set[int]], int]:
    start_beam = lines[0].index("S")
    splitter_sets = []
    for line in lines[2::2]:
        splitter_set = set(m.start() for m in re.finditer(r"\^", line))
        splitter_sets.append(splitter_set)
    return splitter_sets, start_beam


def part_1(splitter_sets: list[set[int]], start_beam: int) -> int:
    total = 0
    current_beams = {start_beam}
    for splitter_set in splitter_sets:
        new_beams = set()
        for current_beam in current_beams:
            if current_beam in splitter_set:
                new_beams.add(current_beam - 1)
                new_beams.add(current_beam + 1)
                total += 1
            else:
                new_beams.add(current_beam)
        current_beams = new_beams
    return total


def part_2(splitter_sets: list[set[int]], start_beam: int) -> int:
    current_beam_strengths = {start_beam: 1}
    for splitter_set in splitter_sets:
        new_beam_strengths = defaultdict(int)
        for current_beam in current_beam_strengths:
            if current_beam in splitter_set:
                new_beam_strengths[current_beam - 1] += current_beam_strengths[current_beam]
                new_beam_strengths[current_beam + 1] += current_beam_strengths[current_beam]
            else:
                new_beam_strengths[current_beam] += current_beam_strengths[current_beam]
        current_beam_strengths = new_beam_strengths
    return sum(current_beam_strengths.values())
