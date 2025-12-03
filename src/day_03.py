def parse(lines: list[str]) -> list[list[int]]:
    banks = [[int(battery_str) for battery_str in line] for line in lines]
    return banks


def calculate_best_output(bank: list[int], battery_count: int = 2) -> int:
    best_batteries = []
    start_index = 0
    end_index = -battery_count + 1
    for i in range(battery_count):
        sub_bank = bank[start_index:end_index] if end_index < 0 else bank[start_index:]
        best_battery = max(sub_bank)
        best_batteries.append(best_battery)
        start_index += sub_bank.index(best_battery) + 1
        end_index += 1
    return int("".join(map(str, best_batteries)))


def part_1(banks: list[list[int]]) -> int:
    return sum(calculate_best_output(bank) for bank in banks)


def part_2(banks: list[list[int]]) -> int:
    return sum(calculate_best_output(bank, battery_count=12) for bank in banks)
