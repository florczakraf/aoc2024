import sys

sum = 0

lines = sys.stdin.read().splitlines()
def count(i, j):
    ds = [(0, 0), (1, 1), (1, 1)]
    s = 0
    y = i
    x = j
    for direction, c in zip(ds, "MAS"):
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

    y = i
    x = j
    for direction, c in zip(ds, "SAM"):
        y += direction[0]
        x += direction[1]

        if y < 0 or y >= len(lines):
            break

        if x < 0 or x >= len(lines[y]):
            break

        if lines[y][x] != c:
            break

        if c == "M":
            s += 1

    ds = [(2, 0), (-1, 1), (-1, 1)]
    y = i
    x = j
    for direction, c in zip(ds, "MAS"):
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

    y = i
    x = j
    for direction, c in zip(ds, "SAM"):
        y += direction[0]
        x += direction[1]

        if y < 0 or y >= len(lines):
            break

        if x < 0 or x >= len(lines[y]):
            break

        if lines[y][x] != c:
            break

        if c == "M":
            s += 1



    if s == 2:
        return 1
    else:
        return 0


for i in range(len(lines)):
    for j, c in enumerate(lines[i]):
        sum += count(i, j)

print(sum)
