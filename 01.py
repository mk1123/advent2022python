from aocd import lines  # type: ignore
import utils
from typing import cast, List
import heapq

doing_part_a = False
actually_submit = True
sample = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

if not actually_submit:
    typed_lines = sample.split("\n")
else:
    typed_lines = cast(List[str], lines)


def a() -> int:
    max_so_far = 0
    curr_sum = 0
    for line in typed_lines:
        if line == "":
            max_so_far = max(max_so_far, curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)
    max_so_far = max(max_so_far, curr_sum)
    return max_so_far


def b() -> int:
    snack_sizes = []
    curr_sum = 0
    for line in typed_lines:
        if line == "":
            if len(snack_sizes) > 2:
                heapq.heappushpop(snack_sizes, curr_sum)
            else:
                heapq.heappush(snack_sizes, curr_sum)
            curr_sum = 0
        else:
            curr_sum += int(line)
    heapq.heappushpop(snack_sizes, curr_sum)
    return sum(snack_sizes)


utils.submit(a() if doing_part_a else b(), actually_submit)
