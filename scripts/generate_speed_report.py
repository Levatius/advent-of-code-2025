import re
from xml.etree import ElementTree

root = ElementTree.parse("speed-report.xml").getroot()

rows = []
for testcase in root.iter("testcase"):
  day = re.match(r"test.test__day_(.+)", testcase.get("classname")).group(1)
  part, test = re.match(r"test__part_(.+)__(.+)", testcase.get("name")).groups()
  time = testcase.get("time")
  status = "passed"

  if testcase.find("failure") is not None:
      status = "failed"
  elif testcase.find("skipped") is not None:
      status = "skipped"

  rows.append((day, part, test, status, time))

lines = [
    "| Day | Part | Test | Status | Time (s) |\n",
    "|-----|------|------|--------|----------|\n",
]
for row in rows:
  lines.append(f"| {" | ".join(row)} |\n")

with open("speed-report.md", "w") as f:
    f.writelines(lines)
