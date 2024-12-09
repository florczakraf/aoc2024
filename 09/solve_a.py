#!/usr/bin/env python3
import sys

dense_line = sys.stdin.read().strip()
sparse_line = []
is_file = True
file_id = 0
target_pos = 0

for c in dense_line:
    length = int(c)
    if is_file:
        sparse_line.extend([file_id] * length)
        file_id += 1
    else:
        sparse_line.extend([None] * length)

    is_file = not is_file

for source_pos in range(len(sparse_line) - 1, 0, -1):
    file_id = sparse_line[source_pos]
    if file_id is None:
        continue

    for i in range(target_pos, source_pos):
        if sparse_line[i] is None:
            target_pos = i
            break
    else:
        break

    sparse_line[target_pos] = file_id
    sparse_line[source_pos] = None
    target_pos += 1

sum = 0
for i, file_id in enumerate(sparse_line):
    if file_id is None:
        break
    sum += i * file_id

print(sum)
