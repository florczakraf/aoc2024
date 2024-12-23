#!/usr/bin/env pypy3
import sys
from collections import defaultdict, Counter
from functools import cache

connections = defaultdict(set)
lines = sys.stdin.read().splitlines()
for line in lines:
    a, b = line.strip().split("-")
    connections[a].add(b)
    connections[b].add(a)

returned = set()
longest = 0
vis = set()
def get_lans(used, rest: frozenset):
    global longest
    if not rest:
        yield used
    else:
        prefix = tuple(sorted(used))
        if prefix not in vis:
            for c in rest:
                is_connected = all(c in connections[prev] for prev in used)
                if is_connected:
                    rc = rest - {c}
                    yield from get_lans(used + (c,), frozenset(rc))
                else:
                    if len(used) > longest:
                        longest = len(used)
                        print(used)
                    yield used
        vis.add(prefix)

lans = set()
for lan in get_lans((), frozenset(connections.keys())):
    lans.add(tuple(sorted(lan)))

largest_len = 0
largest = None
for lan in lans:
    if len(lan) > largest_len:
        largest_len = len(lan)
        largest = lan

print(",".join(largest))
