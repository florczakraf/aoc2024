#!/usr/bin/env python3
import re
import sys

nums = [int(x) for x in re.findall(r"\d+", sys.stdin.read())]
program = nums[3:]

def run(a, b, c, program):
    ip = 0
    out = []

    def get_combo_operand():
        nonlocal ip, program
        ip += 1
        v = program[ip]
        if v < 4:
            return v
        elif v == 4:
            return a
        elif v == 5:
            return b
        elif v == 6:
            return c
        else:
            raise RuntimeError("operand 7 is not supported")

    def get_literal_operand():
        nonlocal ip, program
        ip += 1
        return program[ip]

    while ip < len(program):
        op = program[ip]
        match op:
            case 0:
                a = a // (2 ** get_combo_operand())
            case 1:
                b ^= get_literal_operand()
            case 2:
                b = get_combo_operand() % 8
            case 3:
                operand = get_literal_operand()
                if a != 0:
                    ip = operand
                    continue
            case 4:
                get_literal_operand()
                b ^= c
            case 5:
                v = get_combo_operand() % 8
                out.append(v)
            case 6:
                operand = get_combo_operand()
                b = a // (2 ** operand)
            case 7:
                operand = get_combo_operand()
                c = a // (2 ** operand)

        ip += 1

    return out


candidates = list(range(8))
expected = []
for num in program[::-1]:
    expected = [num] + expected
    next_candidates = []
    for a in candidates:
        result = run(a, 0, 0, program)
        if result == expected:
            if result == program:
                print(a)
                exit(0)
            next_candidates.extend(range(a * 8, a * 8 + 8))
    candidates = next_candidates
