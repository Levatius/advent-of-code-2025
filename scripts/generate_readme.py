import re
from xml.etree import ElementTree

root = ElementTree.parse("tests-report.xml").getroot()

rows = []
for testcase in root.iter("testcase"):
    part, test = re.match(r"test__part_(.+)__(.+)", testcase.get("name")).groups()

    if test != "puzzle_input":
        continue

    day = re.match(r"test.test__day_(.+)", testcase.get("classname")).group(1)
    time = float(testcase.get("time"))

    rows.append((day, part, str(int(time * 1000))))

lines = [
    "| Day | Part | Time (ms) |\n",
    "|-----|------|-----------|\n",
]
for row in rows:
    lines.append(f"| {' | '.join(row)} |\n")

with open("new-README.md", "w") as f:
    f.writelines(lines)
