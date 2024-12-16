#!/usr/bin/env python3
import heapq
import queue
import sys
from collections import defaultdict

lines = sys.stdin.read().splitlines()

clockwise = {
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
}
counterclockwise = {v: k for k, v in clockwise.items()}
start = end = None
dir = (0, 1)
h = len(lines)
w = len(lines[0])

for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == "S":
            start = i, j
        elif c == "E":
            end = i, j

heap = []
heapq.heappush(heap, (0, start, dir))
dists = defaultdict(lambda: float("inf"))
dists[start, dir] = 0

while heap:
    dist, (y, x), (dy, dx) = heapq.heappop(heap)
    if dists[(y, x), (dy, dx)] < dist:
        continue

    yy = y + dy
    xx = x + dx
    if 0 <= yy < h and 0 <= xx < w:
        c = lines[yy][xx]
        if c != "#":
            next_dist = dist + 1
            if next_dist < dists[(yy, xx), (dy, dx)]:
                dists[(yy, xx), (dy, dx)] = next_dist
                heapq.heappush(heap, (next_dist, (yy, xx), (dy, dx)))

    for next_dir in (clockwise[(dy, dx)], counterclockwise[(dy, dx)]):
        next_dist = dist + 1000
        if next_dist < dists[(y, x), next_dir]:
            dists[(y, x), next_dir] = next_dist
            heapq.heappush(heap, (next_dist, (y, x), next_dir))

print(min(dists[end, d] for d in clockwise.keys()))
