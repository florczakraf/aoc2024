import re
import sys

sum = 0

line = sys.stdin.read()
matches = re.finditer(r"mul\((\d+),(\d+)\)", line)
for m in matches:
    if m is not None:
        a = int(m.group(1))
        b = int(m.group(2))
        sum += a * b

print(sum)
