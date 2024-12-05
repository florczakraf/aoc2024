import re
import sys
from collections import defaultdict

sum = 0
manuals = False
rules = defaultdict(set)

def check(pages):
    for i, p in enumerate(pages):
        for p2 in pages[i+1:]:
            if p2 not in rules[p]:
                return 0

    return pages[len(pages) // 2]



lines = sys.stdin.read().splitlines()
for l in lines:
    if not l:
        manuals = True
        continue

    if not manuals:
        a,b = l.split("|")
        rules[int(a)].add(int(b))

    if manuals:
        pages = [int(x) for x in l.split(",")]
        print(l, check(pages))
        sum += check(pages)

print(sum)
