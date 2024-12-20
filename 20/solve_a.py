#!/usr/bin/env python3
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

"""
  x
 x.x
x.@.x
 x.x
  x
"""
skip_map = [
    (-2, 0),
    (-1, 1),
    (0, 2),
    (1, 1),
    (2, 0),
    (1, -1),
    (0, -2),
    (-1, -1),
]

skips = Counter()
for y, x in dists:
    dist = dists[y, x]
    for dy, dx in skip_map:
        yy = y + dy
        xx = x + dx
        skip_dist = dists.get((yy, xx), float("-inf"))
        if skip_dist > dist + 2:
            skips[skip_dist-dist - 2] += 1

s = 0
for skip, n in skips.items():
    if skip >= 100:
        s += n
print(s)
