#!/usr/bin/env python3
import sys
from functools import cache

nums = [int(x) for x in sys.stdin.read().strip().split()]

@cache
def count(n, epoch):
    if epoch == 75:
        return 1

    if n == 0:
        return count(1, epoch + 1)

    sn = str(n)
    ln = len(sn)

    if len(sn)%2 == 0:
        return count(int(sn[:ln//2]), epoch + 1) + count(int(sn[ln//2:]), epoch + 1)

    return count(n * 2024, epoch + 1)

print(sum(count(n, 0) for n in nums))
