#!/usr/bin/env python3
import re
import sys

nums = [int(x) for x in re.findall(r"\d+", sys.stdin.read())]
A, B, C = nums[:3]
program = nums[3:]
ip = 0
out = []

print(program)

def get_combo_operand():
    global ip, program
    ip += 1
    v = program[ip]
    if v < 4:
        return v
    elif v == 4:
        return A
    elif v == 5:
        return B
    elif v == 6:
        return C
    else:
        raise RuntimeError("operand 7 is not supported")

def get_literal_operand():
    global ip, program
    ip += 1
    return program[ip]

while ip < len(program):
    op = program[ip]
    print(f"{ip=} {op=} {A=} {B=} {C=}")
    match op:
        case 0:
            A = A // (2 ** get_combo_operand())
        case 1:
            B ^= get_literal_operand()
        case 2:
            B = get_combo_operand() % 8
        case 3:
            operand = get_literal_operand()
            if A != 0:
                ip = operand
                continue
        case 4:
            get_literal_operand()
            B ^= C
        case 5:
            v = get_combo_operand() % 8
            print(v)
            out.append(v)
        case 6:
            operand = get_combo_operand()
            B = A // (2 ** operand)
        case 7:
            operand = get_combo_operand()
            C = A // (2 ** operand)


    ip += 1

print(f"{A=} {B=} {C=}")
print(",".join(str(x) for x in out))
