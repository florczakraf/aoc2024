import re
import sys

sum = 0

lines = sys.stdin.read().splitlines()
def count(i, j):
    directions_with_diagonals = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1),
    ]
    s = 0
    for direction in directions_with_diagonals:
        y = i
        x = j
        for c in "MAS":
            y += direction[0]
            x += direction[1]

            if y < 0 or y >= len(lines):
                break

            if x < 0 or x >= len(lines[y]):
                break

            if lines[y][x] != c:
                break

            if c == "S":
                s += 1

    return s

for i in range(len(lines)):
    for j, c in enumerate(lines[i]):
        if c == "X":
            sum += count(i, j)

print(sum)
