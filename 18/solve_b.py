#!/usr/bin/env python3
import queue
import sys

size = 70 + 1
n = 1024
# size = 6 + 1
# n = 12

start = 0, 0
end = size - 1, size - 1

walls = []
lines = sys.stdin.read().splitlines()
for l in lines:
    x, y = [int(x) for x in l.split(",")]
    walls.append((y, x))

def bfs(walls):
    walls_set = set(walls)
    q = queue.Queue()
    q.put((*start, 0))
    vis = set()

    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while not q.empty():
        y, x, dist = q.get()
        if (y, x) == end:
            return dist
        if (y, x) in vis:
            continue
        vis.add((y, x))

        for dx, dy in dirs:
            yy = y + dy
            xx = x + dx
            if (yy, xx) not in vis and 0 <= yy < size and 0 <= xx < size and (yy, xx) not in walls_set:
                q.put((yy, xx, dist+1))
    else:
        return -1

# brute-force is "fast enough" on i9 with pypy
# for i in range(n, len(lines)):
#     if bfs(walls[:i+1]) == -1:
#         print(i, lines[i])
#         break

# binsearch
lower = n
upper = len(lines) + 1
while lower <= upper:
    if upper == lower:
        print(upper, lines[upper])
        break
    mid = (lower + upper) // 2
    if bfs(walls[:mid + 1]) == -1:
        upper = mid
    else:
        lower = mid + 1
