import sys
from itertools import cycle

dirs = cycle([[-1, 0], [0, 1], [1, 0], [0, -1]])
dir = next(dirs)
map = [list(l.strip()) for l in sys.stdin.read().splitlines()]
start = pos = None
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "^":
            start = pos = y, x

while True:
    next_pos = pos[0] + dir[0], pos[1] + dir[1]
    inbounds = (0 <= next_pos[0] < len(map)) and (0 <= next_pos[1] < len(map[0]))

    if not inbounds:
        map[pos[0]][pos[1]] = "@"
        break

    c = map[next_pos[0]][next_pos[1]]
    if c == ".":
        map[pos[0]][pos[1]] = "@"
        pos = next_pos
        continue
    elif c == "@":
        map[pos[0]][pos[1]] = "@"
        pos = next_pos
        continue
    elif c == "#":
        dir = next(dirs)
        continue

steps = 0
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "@":
            steps += 1

print(steps)
