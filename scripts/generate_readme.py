import re
from xml.etree import ElementTree

root = ElementTree.parse("tests-report.xml").getroot()

rows = []
for testcase in root.iter("testcase"):
    day = re.match(r"test.test__day_(.+)", testcase.get("classname")).group(1)
    part, test = re.match(r"test__part_(.+)__(.+)", testcase.get("name")).groups()
    time = float(testcase.get("time"))

    rows.append((day, part, test, int(time * 1000)))

lines = [
    "| Day | Part | Test | Time (ms) |\n",
    "|-----|------|------|-----------|\n",
]
for row in rows:
    lines.append(f"| {' | '.join(row)} |\n")

with open("new-README.md", "w") as f:
    f.writelines(lines)
