#!/usr/bin/env pypy3
import sys
from collections import Counter

lines = sys.stdin.read().splitlines()

def step(x):
    x ^= x * 64
    x %= 16777216
    x ^= x // 32
    x %= 16777216
    x ^= x * 2048
    x %= 16777216
    return x


sequences = Counter()
for line in lines:
    x = int(line)
    prev_price = x % 10
    diffs = []
    vis = set()
    for _ in range(2000):
        x = step(x)
        price = x % 10
        diff = price - prev_price
        diffs.append(diff)
        prev_price = price
        if len(diffs) >= 4:
            sequence = tuple(diffs[-4:])
            if sequence not in vis:
                sequences[sequence] += price
                vis.add(sequence)

print(sequences.most_common(1))
