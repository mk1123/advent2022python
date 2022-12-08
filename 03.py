from aocd import lines  # type: ignore
import utils
from typing import cast, List

doing_part_a = False
actually_submit = True
sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

if not actually_submit:
    typed_lines = sample.split("\n")
else:
    typed_lines = cast(List[str], lines)


def get_score_from_char(char: str) -> int:
    return (ord(char) - ord("a") if char.islower() else ord(char) - ord("A") + 26) + 1


def a() -> int:
    total_sum = 0
    for line in typed_lines:
        first_half_set, second_half_set = map(
            set, (line[: len(line) // 2], line[len(line) // 2 :])
        )
        common_elem = list(first_half_set.intersection(second_half_set))[0]
        total_sum += get_score_from_char((common_elem))
    return total_sum


def b() -> int:
    groups = [typed_lines[i : i + 3] for i in range(0, len(typed_lines), 3)]
    total_sum = 0
    for group in groups:
        set_1, set_2, set_3 = map(set, (group[0], group[1], group[2]))
        common_elem = list(set_1.intersection(set_2).intersection(set_3))[0]
        total_sum += get_score_from_char(common_elem)
    return total_sum


utils.submit(a() if doing_part_a else b(), actually_submit)
