from dataclasses import dataclass


@dataclass
class ProductIDRange:
    start: int
    end: int

    @classmethod
    def from_range_str(cls, range_str: str) -> ProductIDRange:
        start_str, end_str = range_str.split("-")
        return cls(int(start_str), int(end_str))

    def find_invalid_product_ids(
        self, max_pattern_repeats: int | None = None
    ) -> set[int]:
        invalid_product_ids = set()
        start_digits = len(str(self.start))
        end_digits = len(str(self.end))
        for id_digits in range(start_digits, end_digits + 1):
            max_repeats = id_digits if not max_pattern_repeats else max_pattern_repeats
            for pattern_repeats in range(2, max_repeats + 1):
                # Skip invalid pattern_repeats for number_digits
                if id_digits % pattern_repeats != 0:
                    continue
                pattern_size = id_digits // pattern_repeats
                for pattern in range(10 ** (pattern_size - 1), 10**pattern_size):
                    # Example: Pattern 12 with 3 repeats generates 121212
                    invalid_product_id = int(str(pattern) * pattern_repeats)
                    if self.start <= invalid_product_id <= self.end:
                        invalid_product_ids.add(invalid_product_id)
        return invalid_product_ids


def parse(lines: list[str]) -> list[ProductIDRange]:
    product_id_ranges = [
        ProductIDRange.from_range_str(range_str) for range_str in lines[0].split(",")
    ]
    return product_id_ranges


def part_1(product_id_ranges: list[ProductIDRange]) -> int:
    total = 0
    for product_id_range in product_id_ranges:
        total += sum(product_id_range.find_invalid_product_ids(max_pattern_repeats=2))
    return total


def part_2(product_id_ranges: list[ProductIDRange]) -> int:
    total = 0
    for product_id_range in product_id_ranges:
        total += sum(product_id_range.find_invalid_product_ids())
    return total
