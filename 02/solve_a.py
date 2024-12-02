import re
import sys

nums = []
sum = 0
for line in sys.stdin.read().splitlines():
    nums_line = [int(x) for x in line.split()]
    nums.append(nums_line)
    if not ((sorted(nums_line) == nums_line) or (sorted(nums_line, reverse=True) == nums_line)):
        continue

    if not all(1 <= abs(a - b) <= 3 for a,b in zip(nums_line[:-1], nums_line[1:])):
        continue
    sum += 1


print(sum)
