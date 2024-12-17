#!/usr/bin/env python3
import re
import sys

import z3

nums = [int(x) for x in re.findall(r"\d+", sys.stdin.read())]
program = nums[3:]

optimizer = z3.Optimize()
solution = z3.BitVec("solution", len(program) * 3)
a = solution
for num in program:
    b = a % 8
    b ^= 5
    c = a >> b
    a /= 8
    b ^= c
    b ^= 6
    optimizer.add((b % 8) == num)
optimizer.minimize(solution)
if optimizer.check() == z3.sat:
    print(optimizer.model().eval(solution))
