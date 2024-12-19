"""
Advent of code 2024 Day 1
"""

with open("inputs/day-1-input-1", "r") as f:
    values = f.read().split()
list_1 = sorted([int(values[i]) for i in range(0, len(values), 2)])
list_2 = sorted([int(values[i]) for i in range(1, len(values), 2)])
answer_1 = sum([abs(list_1[i] - list_2[i]) for i in range(len(list_1))])
print(answer_1)
answer_2 = sum([item * list_2.count(item) for item in list_1])
print(answer_2)