import re
import sys

sum = 0

line = sys.stdin.read()
line = "do()" + line.strip() + "don't()"
dos = line.split("do()")
for d in dos:
    matches = re.finditer(r"mul\((\d+),(\d+)\)", d.split("don't()")[0])
    for m in matches:
        if m is not None:
            a = int(m.group(1))
            b = int(m.group(2))
            sum += a * b

print(sum)
