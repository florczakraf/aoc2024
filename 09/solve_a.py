#!/usr/bin/env python3
import sys
import heapq

dense_line = sys.stdin.read().strip()
sparse_line = []
is_file = True
file_id = 0
free_slots = []
cur = 0

for c in dense_line:
    length = int(c)
    if is_file:
        sparse_line.extend([file_id] * length)
        file_id += 1
    else:
        sparse_line.extend([None] * length)
        free_slots.extend(list(range(cur, cur + length)))

    is_file = not is_file
    cur += length

heapq.heapify(free_slots)

for i in range(len(sparse_line)):
    if not free_slots:
        break

    source_pos = len(sparse_line) - i - 1
    target_pos = heapq.heappop(free_slots)
    file_id = sparse_line[source_pos]
    if file_id is None:
        heapq.heappush(free_slots, target_pos)
        continue

    if target_pos > source_pos:
        break
    sparse_line[target_pos] = file_id
    sparse_line[source_pos] = None
    heapq.heappush(free_slots, source_pos)

sum = 0
for i, file_id in enumerate(sparse_line):
    if file_id is None:
        break
    sum += i * file_id

print(sum)
