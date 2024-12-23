#!/usr/bin/env python3
import sys
from collections import defaultdict

connections = defaultdict(set)
lines = sys.stdin.read().splitlines()
for line in lines:
    a, b = line.strip().split("-")
    connections[a].add(b)
    connections[b].add(a)

def bron_kerbosch(r, p, x):
    if not p and not x:
        yield r

    while p:
        v = p.pop()
        yield from bron_kerbosch(r.union({v}), p.intersection(connections[v]), x.intersection(connections[v]))
        x.add(v)

largest_len = 0
largest = None
for lan in bron_kerbosch(set(), set(connections.keys()), set()):
    if len(lan) > largest_len:
        largest_len = len(lan)
        largest = sorted(lan)


print(",".join(largest))
