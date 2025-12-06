import importlib
import re
import inspect
from pathlib import Path

from aocd import get_data
from aocd.exceptions import PuzzleLockedError


def get_caller_file() -> str:
    frames = inspect.getouterframes(inspect.currentframe())
    caller_file = frames[2].filename
    return caller_file


def get_aoc_imports():
    caller_file = get_caller_file()
    year_str, day_str = re.search(r"advent-of-code-(\d+)\\test\\test__day_(\d+).py", caller_file).groups()
    module = importlib.import_module(f"src.day_{day_str}", str(Path.cwd() / "src" / f"day_{day_str}.py"))
    try:
        puzzle_input_lines = get_data(day=int(day_str), year=int(year_str)).splitlines()
    except PuzzleLockedError:
        puzzle_input_lines = None
    return module.parse, module.part_1, module.part_2, puzzle_input_lines
