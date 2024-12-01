#!/bin/bash
set -Eeuo pipefail

today_zero_pad=$(date +%d)
day_zero_pad=${1:-$today_zero_pad}
mkdir -p "$day_zero_pad"
day=$(echo "$day_zero_pad" | sed 's/^0*//')
curl -fsS -H "cookie: session=$(cat .aoc_cookie)" -o "${day_zero_pad}/input"  "https://adventofcode.com/2024/day/${day}/input"
