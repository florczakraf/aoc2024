#!/usr/bin/env python3
import sys
import re

sum = 0
lines = sys.stdin.read().splitlines()


def check(result, acc, nums):
    a = acc - nums[-1]
    b, m = divmod(acc, nums[-1])
    s = str(acc)
    c = int(s.removesuffix(str(nums[-1])) or "0") if s.endswith(str(nums[-1])) else None

    if len(nums) == 1:
        if a == 0 or (b == 0 and not m) or c == 0:
            return result
        else:
            return 0

    if a > 0:
        ar = check(result, a, nums[:-1])
        if ar == result:
            return result

    if b > 0 and not m:
        br = check(result, b, nums[:-1])
        if br == result:
            return result

    if c is not None and c > 0:
        return check(result, c, nums[:-1])

    return 0


for l in lines:
    nums = [int(x) for x in re.findall(r"\d+", l)]
    sum += check(nums[0], nums[0], nums[1:])

print(sum)
