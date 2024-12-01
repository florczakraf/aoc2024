#!/bin/bash
set -Eeuo pipefail

N=10

for s in $(find . -name '*py' | sort); do
    if [ -f "$s.stats" ]; then
        cat "$s.stats"
        continue
    fi

    echo -n "$s: " >> "$s.stats"
    totals=()
    for _ in $(seq 1 $N); do
        d=$(dirname "$s")
        start=$(date +%s%N)
        python3 "$s" < "$d/input" >/dev/null
        total_ms="$((($(date +%s%N) - "$start")/1000000))"
        totals+=("$total_ms")
        echo -n "$total_ms " >> "$s.stats"
    done
    echo -n "ms | avg: " >> "$s.stats"

    sum=0
    for e in "${totals[@]}"; do
        sum=$(("$sum" + "$e"))
    done
    echo "$(("$sum" / "$N")) ms" >> "$s.stats"

    cat "$s.stats"
done
