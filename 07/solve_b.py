#!/usr/bin/env pypy3
import sys
import re

sum = 0
lines = sys.stdin.read().splitlines()


def check(result, acc, nums):
    a = acc + nums[0]
    b = acc * nums[0]
    c = int(str(acc) + str(nums[0]))

    if len(nums) == 1:
        if a == result or b == result or c == result:
            return result
        else:
            return 0

    if a <= result:
        ar = check(result, a, nums[1:])
        if ar == result:
            return result

    if b <= result:
        br = check(result, b, nums[1:])
        if br == result:
            return result

    if c <= result:
        cr = check(result, c, nums[1:])
        if cr == result:
            return result

    return 0


for l in lines:
    nums = [int(x) for x in re.findall(r"\d+", l)]
    sum += check(nums[0], 0, nums[1:])

print(sum)
