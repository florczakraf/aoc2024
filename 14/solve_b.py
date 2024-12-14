#!/usr/bin/env pypy3
import re
import sys

epochs = 100000
w = 101
h = 103
nums = [int(x) for x in re.findall(r"-?\d+", sys.stdin.read())]
num_robots = len(nums) // 4
for epoch in range(epochs):
    vis = set()
    for i in range(num_robots):
        sx, sy = nums[4*i], nums[4*i + 1]
        vx, vy = nums[4*i + 2], nums[4*i + 3]

        tx = (sx + vx * epoch) % w
        ty = (sy + vy * epoch) % h

        if (ty, tx) in vis:
            break
        vis.add((ty, tx))

    if num_robots == len(vis):
        print(epoch)
        break
