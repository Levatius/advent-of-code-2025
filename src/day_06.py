import operator
from dataclasses import dataclass
from functools import reduce
from itertools import zip_longest
from typing import Callable

OPERATOR_MAP = {
    "+": operator.add,
    "*": operator.mul,
}


@dataclass
class Problem:
    row_numbers: list[int]
    column_numbers: list[int]
    operator: Callable

    @classmethod
    def from_block(cls, block: tuple[str]):
        # Example: block = ["123", " 45", "  6", "*  "]
        operator_char = block[-1].strip()
        number_strs = block[:-1]

        # Example: row_numbers = [123, 45, 6]
        row_numbers = [int(number_str) for number_str in number_strs]
        # Example: column_digits = [("3", "5", "6"), ("2", "4", " "), ("1", " ", " ")]
        column_digits = zip(*(reversed(number_str) for number_str in number_strs))
        # Example: column_numbers = [356, 24, 1]
        column_numbers = [int("".join(digits)) for digits in column_digits]

        return cls(row_numbers, column_numbers, operator=OPERATOR_MAP[operator_char])


def parse(lines: list[str]) -> list[Problem]:
    columns = zip_longest(*lines, fillvalue=" ")
    grouped_columns = [[]]
    for column in columns:
        # Add non-empty columns to last group of columns
        if any(item != " " for item in column):
            grouped_columns[-1].append(column)
        else:
            grouped_columns.append([])
    grouped_rows = [list(zip(*group)) for group in grouped_columns]
    blocks = [["".join(item) for item in column] for column in grouped_rows]
    problems = [Problem.from_block(block) for block in blocks]
    return problems


def part_1(problems: list[Problem]) -> int:
    return sum(reduce(problem.operator, problem.row_numbers) for problem in problems)


def part_2(problems: list[Problem]) -> int:
    return sum(reduce(problem.operator, problem.column_numbers) for problem in problems)
