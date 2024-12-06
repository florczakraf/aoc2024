AoC [readme](https://adventofcode.com/2024/about) says that:
> every problem has a solution that completes in at most 15 seconds on ten-year-old hardware

It happens that one of my computers runs on roughly 10 years old Intel i5-4460 so I decided to use it as a benchmarking machine instead of my daily driver i9-10850k that runs at almost twice the clock.

|task|interpreter|run 1|run 2|run 3|run 4|run 5|avg|
|----|-----------|-----|-----|-----|-----|-----|---|
| ./01/solve_a.py | python3 | 19 ms | 19 ms | 20 ms | 20 ms | 20 ms | **19 ms** |
| ./01/solve_b.py | python3 | 19 ms | 19 ms | 19 ms | 19 ms | 19 ms | **19 ms** |
| ./02/solve_a.py | python3 | 21 ms | 21 ms | 21 ms | 21 ms | 21 ms | **21 ms** |
| ./02/solve_b.py | python3 | 25 ms | 24 ms | 24 ms | 24 ms | 24 ms | **24 ms** |
| ./03/solve_a.py | python3 | 19 ms | 19 ms | 19 ms | 19 ms | 19 ms | **19 ms** |
| ./03/solve_b.py | python3 | 18 ms | 18 ms | 19 ms | 18 ms | 19 ms | **18 ms** |
| ./04/solve_a.py | python3 | 30 ms | 30 ms | 29 ms | 29 ms | 29 ms | **29 ms** |
| ./04/solve_b.py | python3 | 50 ms | 49 ms | 49 ms | 50 ms | 50 ms | **49 ms** |
| ./05/solve_a.py | python3 | 21 ms | 21 ms | 21 ms | 21 ms | 21 ms | **21 ms** |
| ./05/solve_b.py | python3 | 37 ms | 37 ms | 37 ms | 37 ms | 37 ms | **37 ms** |
| ./06/solve_a.py | python3 | 18 ms | 19 ms | 18 ms | 18 ms | 18 ms | **18 ms** |
| ./06/solve_b.py | pypy3 | 2992 ms | 3054 ms | 2933 ms | 3013 ms | 3087 ms | **3015 ms** |
| ./_meta/pypy_startup.py | pypy3 | 41 ms | 41 ms | 41 ms | 41 ms | 41 ms | **41 ms** |
| ./_meta/python_startup.py | python3 | 17 ms | 18 ms | 18 ms | 18 ms | 18 ms | **17 ms** |
