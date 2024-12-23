#!/usr/bin/env pypy3
import sys
from collections import defaultdict

connections = defaultdict(set)
lines = sys.stdin.read().splitlines()
for line in lines:
    a, b = line.strip().split("-")
    connections[a].add(b)
    connections[b].add(a)

def get_lans(used, rest: set):
    if len(used) > 3:
        return StopIteration
    if not rest:
        yield used
    else:
        for c in rest:
            if len(used) > 3:
                continue
            is_connected = all(c in connections[prev] for prev in used)
            if is_connected:
                rc = rest.copy()
                rc.discard(c)
                yield from get_lans(used + [c], rc)
            else:
                yield used

lans = set()
for c in connections.keys():
    if c[0] == "t":
        for n in connections[c]:
            rest = set(connections.keys()).difference(set((c, n)))
            for lan in get_lans([c, n], rest):
                if len(lan) == 3:
                    lans.add(tuple(sorted(lan)))

print(len(lans))
