#!/usr/bin/env python3
import queue
import sys

sum = 0
lines = sys.stdin.read().splitlines()


def bfs(i, j):
    q = queue.Queue()
    s = 0
    dirs = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]
    q.put((i, j, 0))
    while not q.empty():
        i, j, v = q.get()
        if v == 9:
            s += 1
            continue

        for direction in dirs:
            y = i + direction[0]
            x = j + direction[1]

            if y < 0 or y >= len(lines):
                continue

            if x < 0 or x >= len(lines[y]):
                continue

            vn = int(lines[y][x])
            if v + 1 == vn:
                q.put((y, x, vn))

    return s


for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == "0":
            sum += bfs(y, x)

print(sum)
