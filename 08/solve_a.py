#!/usr/bin/env python3
import sys

antinodes = set()
antennas = {}

lines = sys.stdin.read().splitlines()

max_y = len(lines)
max_x = len(lines[0])

for y, l in enumerate(lines):
    for x, c in enumerate(l):
        if c == ".":
            continue
        if c not in antennas:
            antennas[c] = [(y, x)]
        else:
            for yy, xx in antennas[c]:
                dy = y - yy
                dx = x - xx

                cy = y + dy
                cyy = yy - dy

                if dx < 0:
                    cx = x - abs(dx)
                    cxx = xx + abs(dx)
                else:
                    cx = x + abs(dx)
                    cxx = xx - abs(dx)

                if (0 <= cx < max_x) and (0 <= cy < max_y):
                    antinodes.add((cy, cx))

                if (0 <= cxx < max_x) and (0 <= cyy < max_y):
                    antinodes.add((cyy, cxx))

            antennas[c].append((y, x))

print(len(antinodes))
