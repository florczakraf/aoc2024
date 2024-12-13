#!/usr/bin/env python3
import re
import sys

tokens = 0
nums = [int(x) for x in re.findall(r"\d+", sys.stdin.read())]
for i in range(len(nums)//6):
    ax, ay = nums[6*i], nums[6*i + 1]
    bx, by = nums[6*i + 2], nums[6*i + 3]
    px, py = nums[6*i + 4], nums[6*i + 5]

    px += 10000000000000
    py += 10000000000000

    c = (ax * by - bx * ay)
    if c == 0 or by == 0:
        continue

    m = (px * by - bx * py) // c
    n = (py - ay * m) // by

    if m * ax * by + bx * py != m * bx * ay + px * by:
        continue

    if n * by + m * ay != py:
        continue

    t = 3 * m + n
    tokens += t

    print(f"{ax} {ay} {bx} {by} {px} {py} {t}")

print(tokens)
