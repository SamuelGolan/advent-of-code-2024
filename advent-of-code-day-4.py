"""
Advent of code 2024 Day 4
"""


PATTERNS = ["XMAS", "SAMX"]
PATTERNS_2 = ["MAS", "SAM"]


def pattern_search(i: int, j: int, array: list, patterns: str = PATTERNS) -> int:
    match_count = 0
    # forward check
    if j + 4 <= len(array[i]):
        if "".join(array[i][j:j+4]) in patterns:
            match_count += 1
        # diagonal down check
        if i + 4 <= len(array):
            if "".join([array[i + x][j + x] for x in range(4)]) in patterns:
                match_count += 1
        # diagonal up check
        if i >= 3:
            if "".join([array[i - x][j + x] for x in range(4)]) in patterns:
                match_count += 1
    # down check
    if i + 4 <= len(array) and "".join([array[i + x][j] for x in range(4)]) in patterns:
        match_count += 1
    return match_count


def pattern_search_2(i: int, j: int, array: list) -> int:
    match_count = 0
    if 1 <= i < (len(array) - 1) and 1 <= j < (len(array[i]) - 1):
        if "".join([array[i - 1 + x][j - 1 + x] for x in range(3)]) in PATTERNS_2 and "".join(
            [array[i + 1 - x][j - 1 + x] for x in range(3)]) in PATTERNS_2:
            match_count += 1
    return match_count


def input_search(input: list[list]) -> int:
    match_count = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] in ["S", "X"]:
                match_count += pattern_search(i, j, input)
    return match_count


def input_search_2(input) -> int:
    match_count = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] in ["A"]:
                match_count += pattern_search_2(i, j, input)
    return match_count


with open("inputs/day-4-input", "r") as f:
    input = [list(row.strip()) for row in f.readlines()]

answer_1 = input_search(input)
answer_2 = input_search_2(input)
print(f"{answer_1=}")
print(f"{answer_2=}")
