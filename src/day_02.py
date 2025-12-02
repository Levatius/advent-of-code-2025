from dataclasses import dataclass

@dataclass
class ProductIDRange:
    start: int
    end: int

    @classmethod
    def from_range_str(cls, range_str: str) -> ProductIDRange:
        start_str, end_str = range_str.split("-")
        return cls(int(start_str), int(end_str) + 1)


def parse(lines: list[str]) -> list[ProductIDRange]:
    product_id_ranges = [ProductIDRange.from_range_str(range_str) for range_str in lines[0].split(",")]
    return product_id_ranges


def part_1(product_id_ranges: list[ProductIDRange]) -> int:
    total = 0
    for product_id_range in product_id_ranges:
        for i in range(product_id_range.start, product_id_range.end):
            i_str = str(i)
            if len(i_str) % 2 == 0 and i_str[:len(i_str) // 2] == i_str[len(i_str) // 2:]:
                total += i
    return total

def is_invalid(i: int) -> bool:
    i_str = str(i)
    for j in range(1, len(i_str) // 2 + 1):
        if not (factor := len(i_str) / j).is_integer():
            continue
        if i_str == i_str[:j] * int(factor):
            return True
    return False

def part_2(product_id_ranges: list[ProductIDRange]) -> int:
    total = 0
    for product_id_range in product_id_ranges:
        for i in range(product_id_range.start, product_id_range.end):
            if is_invalid(i):
                total += i
    return total
