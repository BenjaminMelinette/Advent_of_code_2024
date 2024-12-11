#!/usr/bin/python3

def main():
    part_1()
    part_2()

def correct_level(level, rules):
    numbers = level.split(",")
    numbers_index = {n: i for i, n in enumerate(numbers)}
    correct = False
    while (correct != True):
        for x, dependencies in rules.items():
            if x in numbers_index:
                for y in dependencies:
                    if y in numbers_index:
                        if numbers_index[x] > numbers_index[y]:
                            temp = numbers[numbers_index[x]]
                            numbers[numbers_index[x]] = numbers[numbers_index[y]]
                            numbers[numbers_index[y]] = temp
                            numbers_index = {n: i for i, n in enumerate(numbers)}
        correct = check_updates(",".join(numbers), rules)
    return ",".join(numbers)

def part_2():
    rules = {}
    levels = []
    delimit = False
    total = 0
    with open("Day_5_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            if line == "\n":
                delimit = True
                continue
            if delimit:
                levels.append(line.strip())
            else:
                x, y = line.strip().split("|")
                if x not in rules:
                    rules[x] = []
                rules[x].append(y)
    for level in levels:
        if (check_updates(level, rules) == False):
            level = correct_level(level, rules)
            total += int(level.split(",")[len(level.split(",")) // 2])
    print(total)

def check_updates(level, rules):
    numbers = level.split(",")
    numbers_index = {n: i for i, n in enumerate(numbers)}
    for x, dependencies in rules.items():
        if x in numbers_index:
            for y in dependencies:
                if y in numbers_index:
                    if numbers_index[x] > numbers_index[y]:
                        return False
    return True

def part_1():
    rules = {}
    levels = []
    delimit = False
    total = 0
    with open("Day_5_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            if line == "\n":
                delimit = True
                continue
            if delimit:
                levels.append(line.strip())
            else:
                x, y = line.strip().split("|")
                if x not in rules:
                    rules[x] = []
                rules[x].append(y)
    for level in levels:
        if (check_updates(level, rules)):
            total += int(level.split(",")[len(level.split(",")) // 2])
    print(total)
    
if __name__ == "__main__":
    main()