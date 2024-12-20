"""
Advent of code 2024 Day 4
"""


PATTERN = "XMAS"

def pattern_search(i: int, j: int, array: list, pattern: str = PATTERN) -> int:
    match_count = 0
    # forward check
    if j + 4 <= len(array[i]):
        if "".join(array[i][j:j+4]) == pattern:
            match_count += 1
        # diagonal down check
        if i + 4 <= len(array):
            if "".join([array[i + x][j + x] for x in range(4)]) == pattern:
                match_count += 1
        # diagonal up check
        if i >= 3:
            if "".join([array[i - x][j + x] for x in range(4)]) == pattern:
                match_count += 1
    # reverse check
    if j >= 3:
        if "".join(reversed(array[i][j-3:j+1])) == pattern:
            match_count += 1
        # diagonal down check
        if i + 4 <= len(array):
            if "".join([array[i + x][j - x] for x in range(4)]) == pattern:
                match_count += 1
        # diagonal up check
        if i >= 3:
            if "".join([array[i - x][j - x] for x in range(4)]) == pattern:
                match_count += 1
    # down check
    if i + 4 <= len(array) and "".join([array[i + x][j] for x in range(4)]) == pattern:
        match_count += 1
    # up check
    if i >= 3 and "".join([array[i - x][j] for x in range(4)]) == pattern:
        match_count += 1
    return match_count


def input_search(input: list[list]) -> int:
    match_count = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "X":
                match_count += pattern_search(i, j, input)
    return match_count


temp = [
    'MMMSXXMASM',
    'MSAMXMSMSA',
    'AMXSXMAAMM',
    'MSAMASMSMX',
    'XMASAMXAMM',
    'XXAMMXXAMA',
    'SMSMSASXSS',
    'SAXAMASAAA',
    'MAMMMXMMMM',
    'MXMXAXMASX',
]
match_count = 0
temp = [list(row) for row in temp]

with open("inputs/day-4-input", "r") as f:
    input = [list(row.strip()) for row in f.readlines()]

answer_1 = input_search(input)
print(f"{answer_1=}")