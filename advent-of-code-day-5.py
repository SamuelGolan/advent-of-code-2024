"""
Advent of code 2024 Day 5
"""

temp = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

with open("inputs/day-5-input", "r") as f:
    input = f.read()


def get_rules_and_updates(input: str) -> tuple[dict, list[list[int]]]:
    rules, updates =  input.split("\n\n")
    rules = [rule.split("|") for rule in rules.split("\n")]
    rules_map = {}
    for rule in rules:
        if rule[1] not in rules_map:
            rules_map[rule[1]] = [rule[0]]
        else:
            rules_map[rule[1]].append(rule[0])
    return rules_map, [[x for x in update.split(",")] for update in updates.split("\n")]


def check_update(rules: dict, update: list[str]) -> int:
    disallowed_pages = []
    for page in update:
        if page in disallowed_pages:
            return 0
        if page in rules:
            disallowed_pages.extend(rules[page])
    return int(update[len(update) // 2])


def correct_update(rules: dict, update: list[str]) -> int:
    disallowed_pages = []
    for count, page in enumerate(update):
        if page in disallowed_pages:
            return correct_update(rules, update[: count - 1] + [update[count]] + [update[count - 1]] + update[count + 1:])
        if page in rules:
            disallowed_pages.extend(rules[page])
    return int(update[len(update) // 2])


def main():
    rules, updates = get_rules_and_updates(input)
    answer_1 = 0
    answer_2 = 0
    for update in updates:
        result = check_update(rules, update)
        answer_1 += result
        if check_update(rules, update) == 0:
            answer_2 += correct_update(rules, update)
    print(f"{answer_1=}")
    print(f"{answer_2=}")


if __name__ == "__main__":
    main()