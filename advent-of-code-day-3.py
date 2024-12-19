"""
Advent of code 2024 Day 2
"""

import re
import operator


pattern = "mul\(\d+,\d+\)"
pattern_1 = "\d+"
pattern_2 = "do()"
pattern_3= "don't()"
with open("inputs/day-3-input", "r") as f:
    input = f.read()

calls = re.findall(pattern, input)
answer_1 = sum([operator.mul(*[int(x) for x in re.findall(pattern_1, call)])
             for call in calls])
print(answer_1)
dont = input.split("don't()")
input = dont[0]
for x in dont[1:]:
    if x.find("do()"):
        for y in x.split("do()")[1:]:
            input += y
calls = re.findall(pattern, input)
answer_2 = sum([operator.mul(*[int(x) for x in re.findall(pattern_1, call)])
             for call in calls])
print(answer_2)

