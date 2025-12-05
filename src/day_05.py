import portion as p


def parse(lines: list[str]) -> tuple[p.Interval, list[int]]:
    break_index = lines.index("")

    fresh_range = p.empty()
    for line in lines[:break_index]:
        fresh_range |= p.closed(*map(int, line.split("-")))

    available_ingredients = [int(line) for line in lines[break_index + 1 :]]

    return fresh_range, available_ingredients


def part_1(fresh_id_range: p.Interval, available_ingredients: list[int]) -> int:
    return sum(available_ingredient in fresh_id_range for available_ingredient in available_ingredients)


def part_2(fresh_id_range: p.Interval, _: list[int]) -> int:
    return sum(sub_range.upper - sub_range.lower + 1 for sub_range in fresh_id_range)
