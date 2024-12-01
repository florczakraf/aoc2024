#!/bin/bash
set -Eeuo pipefail

cat >README.md <<EOF
AoC [readme](https://adventofcode.com/2024/about) says that:
> every problem has a solution that completes in at most 15 seconds on ten-year-old hardware

It happens that one of my computers runs on roughly 10 years old Intel i5-4460 so I decided to use it as a benchmarking machine instead of my daily driver i9-10850k that runs at almost twice the clock.

\`\`\`
$(./bench.sh)
\`\`\`
EOF
