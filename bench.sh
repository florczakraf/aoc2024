#!/bin/bash
set -Eeuo pipefail

N=5

for s in $(find . -name '*py' | sort); do
    if [ -f "$s.stats" ]; then
        cat "$s.stats"
        continue
    fi

    interpreter=$(head -n 1 "$s" | rev | cut -d" " -f 1 | rev)
    echo -ne "| [$s]($s) | $interpreter | " >> "$s.stats"
    totals=()
    for _ in $(seq 1 $N); do
        d=$(dirname "$s")
        start=$(date +%s%N)
        "$s" < "$d/input" >/dev/null
        total_ms="$((($(date +%s%N) - "$start")/1000000))"
        totals+=("$total_ms")
        echo -n "$total_ms ms | " >> "$s.stats"
    done

    sum=0
    for e in "${totals[@]}"; do
        sum=$(("$sum" + "$e"))
    done
    echo "**$(("$sum" / "$N")) ms** |" >> "$s.stats"

    cat "$s.stats"
done
