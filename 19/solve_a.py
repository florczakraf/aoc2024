#!/usr/bin/env python3
import sys
from functools import cache

lines = sys.stdin.read().splitlines()
towels = lines[0].split(", ")

@cache
def has_legal_prefix(s):
    if not s:
        return True

    for t in towels:
        if s.startswith(t) and has_legal_prefix(s[len(t):]):
            return True

    return False

sum = 0
for l in lines[2:]:
    if has_legal_prefix(l):
        sum += 1

print(sum)
