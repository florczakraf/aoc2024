#!/usr/bin/env pypy3
import sys

lines = sys.stdin.read().splitlines()

def step(x):
    x ^= x * 64
    x %= 16777216
    x ^= x // 32
    x %= 16777216
    x ^= x * 2048
    x %= 16777216
    return x

s = 0
for line in lines:
    x = int(line)
    for _ in range(2000):
        x = step(x)
    s += x
print(s)
