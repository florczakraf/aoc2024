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

    used_slot = None
    for i, (slot_pos, slot_length) in enumerate(free_slots):
        if slot_pos > cur:
            drive[cur:cur + length] = [file_id] * length
            break

        if slot_length >= length:
            used_slot = i
            drive[slot_pos:slot_pos + length] = [file_id] * length
            break
    else:
        drive[cur:cur + length] = [file_id] * length

    if used_slot is not None:
        remaining = slot_length - length
        if remaining > 0:
            free_slots[i] = (slot_pos + length, remaining)
        else:
            free_slots.pop(i)

        if not free_slots:
            free_slots.append((cur, length))
            continue

        for i, (slot_pos, slot_length) in enumerate(free_slots[:-1]):
            if slot_pos + slot_length == cur:
                free_slots[i] = (slot_pos, slot_length + length)
                if i + 1 < len(free_slots) and cur + length == free_slots[i + 1][0]:
                    free_slots[i] = (slot_pos, slot_length + length + free_slots[i + 1][1])
                    free_slots.pop(i + 1)
                break
            if i + 1 < len(free_slots) and cur + length == free_slots[i + 1][0]:
                free_slots[i + 1] = (cur, cur + length + free_slots[i + 1][1])
                free_slots.pop(i + 1)
                break
        else:
            free_slots.append((cur, length))
            free_slots.sort()

sum = 0

for i, file_id in enumerate(drive):
    if file_id is None:
        continue
    sum += i * file_id

print(sum)
