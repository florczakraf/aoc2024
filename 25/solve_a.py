#!/usr/bin/env python3
import sys
from collections import Counter

keys = []
locks = []
is_lock = False
acc = None

lines = sys.stdin.read().splitlines() + [""]
for l in lines:
    if not l:
        nums = ()
        for i in sorted(acc):
            nums += (acc[i],)
        if is_lock:
            locks.append(nums)
        else:
            keys.append(nums)
        acc = None
        continue

    if acc is None:
        acc = Counter()
        is_lock = True if l[0] == "#" else False

    for i, c in enumerate(l):
        if c == "#":
            acc[i] += 1

def fits(key, lock):
    if not key:
        return 1

    if key[0] + lock[0] <= 7:
        return fits(key[1:], lock[1:])

    return 0

s = 0
for key in keys:
    for lock in locks:
        s += fits(key, lock)
print(s)
