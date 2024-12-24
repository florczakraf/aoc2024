#!/usr/bin/env python3
import operator
import sys
from graphlib import TopologicalSorter
from pathlib import Path

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
        a, op, b = todo[w]
        wires[w] = OP[op](wires[a], wires[b])

dot_lines = ["digraph graphname {"]
for w, (a, op, b) in todo.items():
    dot_lines.append(f"{a} -> {w} [label=\"{op}\"];")
    dot_lines.append(f"{b} -> {w} [label=\"{op}\"];")
dot_lines.append("}")
Path("graph.dot").write_text("\n".join(dot_lines))

def w2num(prefix):
    out = 0
    for w, v in wires.items():
        if w.startswith(prefix):
            out += 2 ** int(w[1:]) * int(v)
    return out

z = w2num("z")
print(z, bin(z))

x = w2num("x")
print(x, bin(x))

y = w2num("y")
print(y, bin(y))

exp = x + y
print(exp, bin(exp))


for i, (a, b) in enumerate(zip(bin(exp)[2:][::-1], bin(z)[2:][::-1])):
    print(i, a, b)


for i in range(1, 44):
    w = f"z{i:02}"
    a, op, b = todo[w]
    print(w, todo[w])
    if a not in todo:
        print("not in todo a: ", a)
        continue
    if b not in todo:
        print("not in todo b: ", b)
        continue
    if todo[a] == (f"x{i:02}", "XOR", f"y{i:02}") or todo[a] == (f"y{i:02}", "XOR", f"x{i:02}") or todo[b] == (f"x{i:02}", "XOR", f"y{i:02}") or todo[b] == (f"y{i:02}", "XOR", f"x{i:02}"):
        continue
    else:
        print("  ", a, todo[a])
        print("  ", b, todo[b])

# while not fixed:
    # ./solve_b.py < dev_input
    # dot -Tpng -O graph.dot
    # eog graph.dot.png
    # swap nodes in dev_input


# rf-> diff input dev_input2
# 98c98
# < dfb XOR bfn -> hbk
# ---
# > dfb XOR bfn -> z14
# 127c127
# < dvw AND rpg -> z23
# ---
# > dvw AND rpg -> dbb
# 147c147
# < dvw XOR rpg -> dbb
# ---
# > dvw XOR rpg -> z23
# 176c176
# < y18 AND x18 -> z18
# ---
# > y18 AND x18 -> kvn
# 230c230
# < grp XOR fgr -> kvn
# ---
# > grp XOR fgr -> z18
# 247c247
# < y34 AND x34 -> cvh
# ---
# > y34 AND x34 -> tfn
# 272c272
# < x34 XOR y34 -> tfn
# ---
# > x34 XOR y34 -> cvh
# 279c279
# < sjr OR tck -> z14
# ---
# > sjr OR tck -> hbk
# (jorah)[~/proj/aoc2024/24]
# rf-> echo -e "hbk\nz14\nz23\ndbb\nz18\nkvn\ncvh\ntfn" | sort | tr '\n' ','
# cvh,dbb,hbk,kvn,tfn,z14,z18,z23,
