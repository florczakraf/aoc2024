import sys
from collections import defaultdict
from graphlib import TopologicalSorter

sum = 0
manuals = False
rules = defaultdict(set)

def check(pages):
    for i, p in enumerate(pages):
        for p2 in pages[i+1:]:
            if p2 not in rules[p]:
                return 0

    return pages[len(pages) // 2]

def fixup(pages):
    ts = TopologicalSorter({k: v for k, v in rules.items() if k in pages})
    order = list(ts.static_order())
    new_pages = sorted(pages, key=order.index, reverse=True)
    print(new_pages)
    return new_pages[len(new_pages)//2]

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

        if check(pages) == 0:
            f = fixup(pages)
            print(l, f)
            sum += f

print(sum)
