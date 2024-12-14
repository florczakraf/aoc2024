#!/usr/bin/env python3
import operator
import re
import sys
from collections import Counter, defaultdict
from functools import reduce

epochs = 100
w = 101
h = 103
nums = [int(x) for x in re.findall(r"-?\d+", sys.stdin.read())]
pos = Counter()
for i in range(len(nums)//4):
    sx, sy = nums[4*i], nums[4*i + 1]
    vx, vy = nums[4*i + 2], nums[4*i + 3]

    tx = (sx + vx * epochs) % w
    ty = (sy + vy * epochs) % h

    pos[(ty, tx)] += 1

qs = defaultdict(int)

for (y, x), n in pos.items():
    if y == h // 2 or x == w // 2:
        continue

    a = y < (h // 2)
    b = x < (w // 2)
    qs[a, b] += n

print(list(qs.items()))
print(reduce(operator.mul, qs.values(), 1))
