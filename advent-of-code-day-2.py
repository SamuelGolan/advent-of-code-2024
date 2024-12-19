"""
Advent of code 2024 Day 2
"""


def determine_safe(report: list[int]) -> int:
    for i in range(len(report) - 1):
        if not 0 < abs(report[i] - report[i + 1]) < 4:
            return 0
    if report == sorted(report) or report == sorted(report, reverse=True):
        return 1
    return 0


def dampen(report: list[int]) -> int:
    if determine_safe(report):
        return 1
    for i in range(1, len(report) + 1):
        if determine_safe(report[0:i - 1] + report[i:len(report)]):
            return 1
    return 0


with open("inputs/day-2-input", "r") as f:
    lines = [[int(item) for item in line.split()] for line in f.readlines()]
answer_1 = sum(determine_safe(report) for report in lines)
print(answer_1)
answer_2 = sum(dampen(report) for report in lines)
print(answer_2)