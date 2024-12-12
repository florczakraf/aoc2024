#!/usr/bin/env python3
import sys
from collections import defaultdict

sum = 0
lines = sys.stdin.read().splitlines()

h = len(lines)
w = len(lines[0])

dirs = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
)

R = (0, 1)
D = (1, 0)

side_dirs = {
    (1, 0): (1, R),
    (-1, 0): (1, R),
    (0, 1): (0, D),
    (0, -1): (0, D),
}


vis = set()
c = None
for i in range(h):
    for j in range(w):
        if (i, j) not in vis:
            c = lines[i][j]
            s = [(i, j)]
            area = 0
            side_map = defaultdict(set)
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
                        side_map[d].add((y, x))
                        continue

                    if lines[yy][xx] == c:
                        s.append((yy, xx))
                    else:
                        side_map[d].add((y, x))


            sides = 0
            for side, fields in side_map.items():
                sort_index, d = side_dirs[side]
                sorted_fields = sorted(fields, key=lambda f: (f[1-sort_index], f[sort_index]))
                y, x = sorted_fields[0]
                sides += 1
                for yy, xx in sorted_fields[1:]:
                    if (y + d[0], x + d[1]) != (yy, xx):
                        sides += 1
                    y, x = yy, xx

            val = area * sides
            print(c, area, sides, val)
            sum += val

print(sum)
