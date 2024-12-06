import sys
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from itertools import cycle

map = [list(l.strip()) for l in sys.stdin.read().splitlines()]
start = pos = None
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == "^":
            start = pos = y, x

loops = 0

def check_loop(guard_candidate):
    print(guard_candidate)
    dirs = cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))
    dir = next(dirs)
    pos = start
    vis = set()

    while True:
        if (pos, dir) in vis:
            return 1

        vis.add((pos, dir))

        next_pos = pos[0] + dir[0], pos[1] + dir[1]
        if not ((0 <= next_pos[0] < len(map)) and (0 <= next_pos[1] < len(map[0]))):
            return 0

        if map[next_pos[0]][next_pos[1]] == "#" or next_pos == guard_candidate:
            dir = next(dirs)
        else:
            pos = next_pos

pool = ProcessPoolExecutor(max_workers=10)
candidates = []
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] in "^#":
            continue
        candidates.append((y, x))

print(sum(pool.map(check_loop, candidates)))
