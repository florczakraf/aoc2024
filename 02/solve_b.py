#!/usr/bin/env python3
import re
import sys

nums = []
sum = 0

def is_safe(nums_line):
    if not ((sorted(nums_line) == nums_line) or (sorted(nums_line, reverse=True) == nums_line)):
        return False

    if not all(1 <= abs(a - b) <= 3 for a,b in zip(nums_line[:-1], nums_line[1:])):
        return False

    return True


for line in sys.stdin.read().splitlines():
    nums_line = [int(x) for x in line.split()]
    nums.append(nums_line)

    if not is_safe(nums_line):
        for i in range(len(nums_line)):
            if is_safe(nums_line[:i] + nums_line[i+1:]):
                sum +=1
                break
    else:
        sum += 1


print(sum)
