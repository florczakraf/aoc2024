#!/usr/bin/env python3
import sys

sum = 0
parse_moves = False
dirs = {
    "<": (0, -1),
    ">": (0, 1),
    "^": (-1, 0),
    "v": (1, 0),
}
map = []
y, x = None, None

lines = sys.stdin.read().splitlines()
for i, l in enumerate(lines):
    if not l:
        parse_moves = True
        continue

    if not parse_moves:
        map.append([])
        for j, c in enumerate(l):
            if c == "@":
                y, x = i, j
                map[-1].append(".")
            else:
                map[-1].append(c)

    if parse_moves:
        for c in l:
            dir = dirs[c]
            ny = y + dir[0]
            nx = x + dir[1]

            next = map[ny][nx]
            if next == ".":
                y = ny
                x = nx
                continue
            elif next == "#":
                continue
            else:
                yy = y
                xx = x
                while next == "O":
                    yy += dir[0]
                    xx += dir[1]
                    next = map[yy][xx]

                if next == ".":
                    map[ny][nx] = "."
                    map[yy][xx] = "O"
                    y = ny
                    x = nx

for i, l in enumerate(map):
    for j, c in enumerate(l):
        if c == "O":
            sum += 100 * i + j

print(sum)
