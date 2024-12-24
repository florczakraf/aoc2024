#!/usr/bin/env python3
import operator
import sys
from graphlib import TopologicalSorter

ops = False
wires = {}
todo = {}
ts = TopologicalSorter()

OP = {
    "AND": operator.and_,
    "OR": operator.or_,
    "XOR": operator.xor,
}

lines = sys.stdin.read().splitlines()
for l in lines:
    if not l:
        ops = True
        continue

    if not ops:
        w, v = l.split(": ")
        wires[w] = int(v)

    if ops:
        a, op, b, _,  w = l.split(" ")
        todo[w] = (a, op, b)
        ts.add(w, a, b)


for w in ts.static_order():
    if w in todo:
        a, op, b = todo.pop(w)
        wires[w] = OP[op](wires[a], wires[b])

out = 0
print(wires)
for w, v in wires.items():
    if w.startswith("z"):
        out += 2**int(w[1:]) * int(v)

print(out)
