#!/usr/bin/env python3
import sys
from functools import cache
from itertools import permutations

lines = sys.stdin.read().splitlines()
numpad_lines = ["789", "456", "123", " 0A"]
arrows_lines = [" ^A", "<v>"]
numpad = {c: (y, x) for y, l in enumerate(numpad_lines) for x, c in enumerate(l) if c != " "}
arrows = {c: (y, x) for y, l in enumerate(arrows_lines) for x, c in enumerate(l) if c != " "}
button_to_dir = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0),
}

@cache
def get_path_len(is_numpad, steps, epoch, start):
    if not steps:
        return 0

    if is_numpad:
        g = numpad
    else:
        g = arrows

    y, x = start
    neighbor = g[steps[0]]
    dy, dx = neighbor[0] - y, neighbor[1] - x
    keys = ""
    if dy >= 0:
        keys += "v" * dy
    else:
        keys += "^" * -dy

    if dx >= 0:
        keys += ">" * dx
    else:
        keys += "<" * -dx

    if epoch == 0:
        presses = len(keys) + 1
    else:
        presses = float("inf")
        for candidate in set(permutations(keys)):
            y, x = start
            valid = True
            for button in candidate:
                dy, dx = button_to_dir[button]
                y += dy
                x += dx
                if (y, x) not in g.values():
                    valid = False
                    break
            if not valid:
                continue

            v = get_path_len(is_numpad=False, steps=candidate + ("A", ), epoch=epoch-1, start=arrows["A"])
            if v < presses:
                presses = v

    return presses + get_path_len(is_numpad, steps[1:], epoch, neighbor)


s = 0
for l in lines:
    path_len = get_path_len(is_numpad=True, steps=l, epoch=25, start=numpad["A"])
    num = int(l[:-1])
    s += path_len * num
    print(l, path_len, path_len * num)
print(s)