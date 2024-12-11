#!/usr/bin/env python3
import sys

nums = [int(x) for x in sys.stdin.read().strip().split()]

def step(n):
    sn = str(n)
    ln = len(sn)
    if n == 0:
        return [1]
    elif len(sn)%2 == 0:
        return [int(sn[:ln//2]), int(sn[ln//2:])]
    else:
        return [n * 2024]


for i in range(25):
    next_nums = []

    for n in nums:
        next_nums.extend(step(n))

    nums = next_nums

print(len(nums))
