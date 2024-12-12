#!/usr/bin/env python3
import sys

sum = 0
lines = sys.stdin.read().splitlines()

h = len(lines)
w = len(lines[0])

areas = []
dirs = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
)
vis = set()
c = None
for i in range(h):
    for j in range(w):
        if (i, j) not in vis:
            c = lines[i][j]
            s = [(i, j)]
            area = 0
            perimeter = 0
            while s:
                y, x = s.pop()
                if (y, x) not in vis:
                    area += 1
                else:
                    continue
                vis.add((y, x))
                for d in dirs:
                    yy = y + d[0]
                    xx = x + d[1]
                    if yy < 0 or yy == h or xx < 0 or xx == w:
                        perimeter += 1
                        continue

                    if lines[yy][xx] == c:
                        s.append((yy, xx))
                    else:
                        perimeter += 1

            val = area*perimeter
            print(c, area, perimeter, val)
            sum += val

print(sum)