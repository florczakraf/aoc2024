#!/usr/bin/env python3
import sys
from functools import cache

lines = sys.stdin.read().splitlines()
towels = lines[0].split(", ")

@cache
def possible_combinations(s):
    if not s:
        return 1

    possible = 0
    for t in towels:
        if s.startswith(t):
            possible += possible_combinations(s[len(t):])

    return possible

sum = 0
for l in lines[2:]:
    sum += possible_combinations(l)

print(sum)
