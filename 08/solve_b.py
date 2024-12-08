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
                cy = cyy = y
                cx = cxx = x

                while (0 <= cx < max_x) and (0 <= cy < max_y):
                    antinodes.add((cy, cx))
                    cy += dy
                    if dx < 0:
                        cx -= abs(dx)
                    else:
                        cx += abs(dx)

                while (0 <= cxx < max_x) and (0 <= cyy < max_y):
                    antinodes.add((cyy, cxx))
                    cyy -= dy
                    if dx < 0:
                        cxx += abs(dx)
                    else:
                        cxx -= abs(dx)

            antennas[c].append((y, x))

print(len(antinodes))
