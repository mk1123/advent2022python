from aocd import lines  # type: ignore
import utils
from typing import cast, List
from enum import Enum
from typing import Union, Literal, Dict

doing_part_a = False
actually_submit = True
sample = """A Y
B X
C Z"""


if not actually_submit:
    typed_lines = sample.split("\n")
else:
    typed_lines = cast(List[str], lines)


class Moves(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Winner(Enum):
    P1 = 1
    P2 = 2
    TIE = 3


scores_for_move = {Moves.ROCK: 1, Moves.PAPER: 2, Moves.SCISSORS: 3}
p1_string_to_move: Dict[Union[Literal["A"], Literal["B"], Literal["C"]], Moves] = {
    "A": Moves.ROCK,
    "B": Moves.PAPER,
    "C": Moves.SCISSORS,
}
p2_string_to_move = {"X": Moves.ROCK, "Y": Moves.PAPER, "Z": Moves.SCISSORS}
winner_string_to_winner = {"X": Winner.P1, "Y": Winner.TIE, "Z": Winner.P2}
winner_from_matchup: Dict[Moves, Dict[Moves, Winner]] = {
    Moves.ROCK: {
        Moves.ROCK: Winner.TIE,
        Moves.PAPER: Winner.P2,
        Moves.SCISSORS: Winner.P1,
    },
    Moves.PAPER: {
        Moves.ROCK: Winner.P1,
        Moves.PAPER: Winner.TIE,
        Moves.SCISSORS: Winner.P2,
    },
    Moves.SCISSORS: {
        Moves.ROCK: Winner.P2,
        Moves.PAPER: Winner.P1,
        Moves.SCISSORS: Winner.TIE,
    },
}

p2_move_from_p1_move_and_winner = {
    move: {v: k for k, v in p2_to_winner.items()}
    for move, p2_to_winner in winner_from_matchup.items()
}

winner_to_score: Dict[Winner, int] = {Winner.P1: 0, Winner.P2: 6, Winner.TIE: 3}


def a() -> int:
    total_score = 0
    for line in typed_lines:
        p1_string, p2_string = line[0], line[2]
        p1_move, p2_move = p1_string_to_move[p1_string], p2_string_to_move[p2_string]
        total_score += (
            winner_to_score[winner_from_matchup[p1_move][p2_move]]
            + scores_for_move[p2_move]
        )
    return total_score


def b() -> int:
    total_score = 0
    for line in typed_lines:
        p1_string, winner_string = line[0], line[2]
        p1_move, winner = (
            p1_string_to_move[p1_string],
            winner_string_to_winner[winner_string],
        )
        p2_move = p2_move_from_p1_move_and_winner[p1_move][winner]
        total_score += winner_to_score[winner] + scores_for_move[p2_move]
    return total_score


utils.submit(a() if doing_part_a else b(), actually_submit)
