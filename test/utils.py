import importlib
import re
import traceback
from pathlib import Path

from aocd import get_data
from aocd.exceptions import PuzzleLockedError


def get_caller_path() -> Path:
    for frame_summary in traceback.extract_stack():
        path = Path(frame_summary.filename)
        if "test__day" in path.stem:
            return path


def get_aoc_imports():
    caller_path = get_caller_path()
    day = int(re.search(r"\d+", caller_path.stem)[0])
    year = int(re.search(r"\d+", caller_path.parent.parent.stem)[0])
    day_filename = f"day_{day:02}"
    module = importlib.import_module(f"src.{day_filename}", str(Path.cwd() / "src" / f"{day_filename}.py"))
    try:
        puzzle_input_lines = get_data(day=day, year=year).splitlines()
    except PuzzleLockedError:
        puzzle_input_lines = None
    return module.parse, module.part_1, module.part_2, puzzle_input_lines