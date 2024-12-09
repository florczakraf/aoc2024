#!/usr/bin/env pypy3
import sys

dense_line = sys.stdin.read().strip()
files = []
is_file = True
file_id = 0
free_slots = []
cur = 0
total_size = 0

for c in dense_line:
    length = int(c)
    if is_file:
        files.append((cur, length, file_id))
        file_id += 1
    else:
        if length > 0:
            free_slots.append((cur, length))

    is_file = not is_file
    cur += length
total_size = cur
drive = [None] * total_size

for cur, length, file_id in files[::-1]:
    if not free_slots or free_slots[0][0] > cur:
        drive[cur:cur + length] = [file_id] * length
        continue

    for i, (slot_pos, slot_length) in enumerate(free_slots):
        if slot_pos > cur:
            drive[cur:cur + length] = [file_id] * length
            break

        if slot_length >= length:
            remaining = slot_length - length
            if remaining > 0:
                free_slots[i] = (slot_pos + length, remaining)
            else:
                free_slots.pop(i)

            drive[slot_pos:slot_pos + length] = [file_id] * length
            break

sum = 0

for i, file_id in enumerate(drive):
    if file_id is None:
        continue
    sum += i * file_id

print(sum)
