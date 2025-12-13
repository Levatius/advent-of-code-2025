import itertools
import re
from collections import Counter
from dataclasses import dataclass

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


@dataclass
class Machine:
    indicators: set[int]
    buttons: list[set[int]]
    requirements: list[int]

    @classmethod
    def from_line(cls, line: str):
        indicators_str, buttons_str, requirements_str = re.match(r"\[([.#]+)] (\(.+\))+ \{(.+)}", line).groups()
        indicators = set(i for i, indicator in enumerate(indicators_str) if indicator == "#")
        buttons = []
        for button_str in buttons_str.split():
            button = set(map(int, button_str.strip("()").split(",")))
            buttons.append(button)
        requirements = list(map(int, requirements_str.split(",")))
        return cls(indicators, buttons, requirements)

    def calculate_min_for_indicators(self) -> int | None:
        for i in range(1, len(self.buttons) + 1):
            for button_combo in itertools.combinations(self.buttons, i):
                counter = Counter()
                for button in button_combo:
                    counter.update(button)
                indicators = {indicator for indicator, count in counter.items() if count % 2 != 0}
                if indicators == self.indicators:
                    return i
        return None

    def calculate_min_for_requirements(self) -> int:
        number_of_buttons = len(self.buttons)
        number_of_requirements = len(self.requirements)

        binary_button_list = [[int(i in button) for i in range(number_of_requirements)] for button in self.buttons]
        A = np.array(binary_button_list).T
        b = np.array(self.requirements)
        c = np.ones(number_of_buttons)

        # Integer variables with lower bound 0
        integrality = np.ones(number_of_buttons, dtype=int)
        bounds = Bounds(lb=np.zeros(number_of_buttons), ub=np.full(number_of_buttons, np.inf))

        # Equality constraints: A @ x == b
        constraints = LinearConstraint(A, lb=b, ub=b)

        result = milp(
            c=c,
            integrality=integrality,
            bounds=bounds,
            constraints=constraints,
        )

        # Assuming there is a solution
        assert result.success

        return int(np.sum(np.round(result.x)))


def parse(lines: list[str]) -> list[Machine]:
    return [Machine.from_line(line) for line in lines]


def part_1(machines: list[Machine]) -> int:
    return sum(machine.calculate_min_for_indicators() for machine in machines)


def part_2(machines: list[Machine]) -> int:
    return sum(machine.calculate_min_for_requirements() for machine in machines)
