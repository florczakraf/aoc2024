#!/usr/bin/env pypy3
import queue
import sys
from collections import Counter

lines = sys.stdin.read().splitlines()
start = end = None

for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == "S":
            start = i, j
        elif c == "E":
            end = i, j

dists = {}
q = queue.Queue()
dirs = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]
q.put((start[0], start[1], 0))
while not q.empty():
    i, j, v = q.get()
    if (i, j) in dists:
        continue

    dists[i, j] = v

    for direction in dirs:
        y = i + direction[0]
        x = j + direction[1]
        if lines[y][x] != "#":
            q.put((y, x, v + 1))

skips = Counter()
for y, x in dists:
    dist = dists[y, x]
    used = set()

    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            for a in range(2, 21):
                for b in range(a+1):
                    yy = y + dy * b
                    xx = x + dx * (a-b)
                    if (yy, xx) in used:
                        continue
                    skip_dist = dists.get((yy, xx), float("-inf"))
                    if skip_dist > dist + a:
                        skips[skip_dist-dist - a] += 1
                        used.add((yy, xx))

s = 0
for skip, n in skips.items():
    if skip >= 100:
        s += n
print(s)
