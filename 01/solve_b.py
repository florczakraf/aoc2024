#!/usr/bin/env python3
import re
import sys
from collections import Counter

l = []
c = Counter()
for line in sys.stdin.read().splitlines():
    a, b = line.split()
    l.append(int(a))
    c[int(b)] += 1

sum = 0

for a in l:
    sum += a * c[a]

print(sum)
