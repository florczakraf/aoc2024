AoC [readme](https://adventofcode.com/2024/about) says that:
> every problem has a solution that completes in at most 15 seconds on ten-year-old hardware

It happens that one of my computers runs on roughly 10 years old Intel i5-4460 so I decided to use it as a benchmarking machine instead of my daily driver i9-10850k that runs at almost twice the clock.

|task|interpreter|run 1|run 2|run 3|run 4|run 5|avg|
|----|-----------|-----|-----|-----|-----|-----|---|
| [./01/solve_a.py](./01/solve_a.py) | python3 | 19 ms | 18 ms | 18 ms | 19 ms | 18 ms | **18 ms** |
| [./01/solve_b.py](./01/solve_b.py) | python3 | 19 ms | 18 ms | 19 ms | 19 ms | 19 ms | **18 ms** |
| [./02/solve_a.py](./02/solve_a.py) | python3 | 20 ms | 20 ms | 20 ms | 20 ms | 20 ms | **20 ms** |
| [./02/solve_b.py](./02/solve_b.py) | python3 | 23 ms | 23 ms | 23 ms | 23 ms | 23 ms | **23 ms** |
| [./03/solve_a.py](./03/solve_a.py) | python3 | 18 ms | 18 ms | 18 ms | 18 ms | 18 ms | **18 ms** |
| [./03/solve_b.py](./03/solve_b.py) | python3 | 18 ms | 18 ms | 18 ms | 18 ms | 18 ms | **18 ms** |
| [./04/solve_a.py](./04/solve_a.py) | python3 | 29 ms | 29 ms | 29 ms | 29 ms | 29 ms | **29 ms** |
| [./04/solve_b.py](./04/solve_b.py) | python3 | 49 ms | 50 ms | 50 ms | 50 ms | 50 ms | **49 ms** |
| [./05/solve_a.py](./05/solve_a.py) | python3 | 21 ms | 21 ms | 21 ms | 21 ms | 21 ms | **21 ms** |
| [./05/solve_b.py](./05/solve_b.py) | python3 | 37 ms | 37 ms | 37 ms | 36 ms | 37 ms | **36 ms** |
| [./06/solve_a.py](./06/solve_a.py) | python3 | 18 ms | 18 ms | 19 ms | 19 ms | 18 ms | **18 ms** |
| [./06/solve_b.py](./06/solve_b.py) | pypy3 | 2917 ms | 3008 ms | 2921 ms | 2960 ms | 3181 ms | **2997 ms** |
| [./07/solve_a.py](./07/solve_a.py) | python3 | 27 ms | 27 ms | 26 ms | 26 ms | 26 ms | **26 ms** |
| [./07/solve_b.py](./07/solve_b.py) | python3 | 35 ms | 35 ms | 35 ms | 35 ms | 35 ms | **35 ms** |
| [./08/solve_a.py](./08/solve_a.py) | python3 | 12 ms | 12 ms | 12 ms | 12 ms | 12 ms | **12 ms** |
| [./08/solve_b.py](./08/solve_b.py) | python3 | 13 ms | 13 ms | 13 ms | 13 ms | 13 ms | **13 ms** |
| [./09/solve_a.py](./09/solve_a.py) | python3 | 42 ms | 43 ms | 44 ms | 43 ms | 45 ms | **43 ms** |
| [./09/solve_b.py](./09/solve_b.py) | pypy3 | 71 ms | 72 ms | 71 ms | 72 ms | 71 ms | **71 ms** |
| [./10/solve_a.py](./10/solve_a.py) | python3 | 33 ms | 33 ms | 33 ms | 33 ms | 33 ms | **33 ms** |
| [./10/solve_b.py](./10/solve_b.py) | python3 | 37 ms | 37 ms | 37 ms | 37 ms | 37 ms | **37 ms** |
| [./11/solve_a.py](./11/solve_a.py) | python3 | 190 ms | 187 ms | 186 ms | 189 ms | 190 ms | **188 ms** |
| [./11/solve_b.py](./11/solve_b.py) | python3 | 136 ms | 137 ms | 137 ms | 135 ms | 135 ms | **136 ms** |
| [./12/solve_a.py](./12/solve_a.py) | python3 | 62 ms | 60 ms | 63 ms | 61 ms | 60 ms | **61 ms** |
| [./12/solve_b.py](./12/solve_b.py) | python3 | 73 ms | 75 ms | 73 ms | 74 ms | 78 ms | **74 ms** |
| [./13/solve_a.py](./13/solve_a.py) | python3 | 19 ms | 19 ms | 19 ms | 19 ms | 19 ms | **19 ms** |
| [./13/solve_b.py](./13/solve_b.py) | python3 | 19 ms | 19 ms | 19 ms | 19 ms | 19 ms | **19 ms** |
| [./14/solve_a.py](./14/solve_a.py) | python3 | 19 ms | 19 ms | 19 ms | 19 ms | 19 ms | **19 ms** |
| [./14/solve_b.py](./14/solve_b.py) | pypy3 | 126 ms | 127 ms | 126 ms | 127 ms | 128 ms | **126 ms** |
| [./_meta/pypy_startup.py](./_meta/pypy_startup.py) | pypy3 | 40 ms | 39 ms | 40 ms | 40 ms | 40 ms | **39 ms** |
| [./_meta/python_startup.py](./_meta/python_startup.py) | python3 | 17 ms | 17 ms | 17 ms | 17 ms | 17 ms | **17 ms** |
