#!/usr/bin/env python3
import queue
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
                y, x = i, j * 2
                map[-1].append(".")
                map[-1].append(".")
            elif c == "O":
                map[-1].append("[")
                map[-1].append("]")
            else:
                map[-1].append(c)
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
            elif next == "#":
                continue
            elif dir in ((0, 1), (0, -1)):
                xx = x
                while next in "[]":
                    xx += dir[1]
                    next = map[y][xx]

                if next == ".":
                    map[y].pop(xx)
                    map[y].insert(nx, ".")
                    y = ny
                    x = nx
            else:
                q = queue.Queue()
                boxes = []
                dy = dir[0]
                can_move = True
                if next == "]":
                    box = ny, nx-1
                else:
                    box = ny, nx
                q.put(box)

                while not q.empty() and can_move:
                    yy, xx = q.get()
                    if (yy, xx) in boxes:
                        continue
                    boxes.append((yy, xx))
                    nyy = yy + dy

                    if map[nyy][xx] == map[nyy][xx+1] == ".":
                        continue
                    if (map[nyy][xx] == "#") or (map[nyy][xx+1] == "#"):
                        can_move = False
                        break

                    if map[nyy][xx] == "[":
                        q.put((nyy, xx))
                    elif map[nyy][xx] == "]":
                        q.put((nyy, xx-1))

                    if map[nyy][xx+1] == "[":
                        q.put((nyy, xx+1))

                if can_move:
                    for box in boxes[::-1]:
                        map[box[0] + dy][box[1]] = map[box[0]][box[1]]
                        map[box[0] + dy][box[1] + 1] = map[box[0]][box[1] + 1]
                        map[box[0]][box[1]] = "."
                        map[box[0]][box[1] + 1] = "."
                    y = ny

for i, l in enumerate(map):
    for j, c in enumerate(l):
        if c == "[":
            sum += 100 * i + j

print(sum)
