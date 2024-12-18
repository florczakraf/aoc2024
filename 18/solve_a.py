#!/usr/bin/env python3
import queue
import sys

size = 70 + 1
n = 1024
start = 0, 0
end = size - 1, size - 1

map = [["." for __ in range(size)] for _ in range(size)]
lines = sys.stdin.read().splitlines()
for l in lines[:n]:
    x, y = [int(x) for x in l.split(",")]
    map[y][x] = "#"

q = queue.Queue()
q.put((*start, 0))
vis = set()

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

while not q.empty():
    y, x, dist = q.get()
    if (y, x) == end:
        print(dist)
        break
    if (y, x) in vis:
        continue
    vis.add((y, x))

    for dx, dy in dirs:
        yy = y + dy
        xx = x + dx
        if (yy, xx) not in vis and 0 <= yy < size and 0 <= xx < size and map[yy][xx] == ".":
            q.put((yy, xx, dist+1))

for l in map:
    print("".join(l))
