#!/usr/bin/env python3
import re
import sys

l, r = [], []
for line in sys.stdin.read().splitlines():
    a, b = line.split()
    l.append(int(a))
    r.append(int(b))

l = sorted(l)
r = sorted(r)

sum = 0

for a, b in zip(l, r):
    sum += abs(a - b)

print(sum)
