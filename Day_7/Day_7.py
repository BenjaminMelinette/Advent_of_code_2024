#!/usr/bin/python3

from itertools import product

def main():
    part_1()
    part_2()

def part_2():
    total = 0
    with open("Day_7_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            goal, numbers = line.split(": ")
            goal = int(goal)
            numbers = [int(n) for n in numbers.split(" ")]
            if (is_solution_2(goal, numbers)):
                total += goal
    print(total)
    return

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '|':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def is_solution_2(goal, numbers):
    operator_combinations = product('+*|', repeat=len(numbers) - 1)
    for ops in operator_combinations:
        if evaluate_expression(numbers, ops) == goal:
            return True
    return False

def is_solution(goal, numbers):
    operator_combinations = product('+*', repeat=len(numbers) - 1)
    for ops in operator_combinations:
        if evaluate_expression(numbers, ops) == goal:
            return True
    return False

def part_1():
    total = 0
    with open("Day_7_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            goal, numbers = line.split(": ")
            goal = int(goal)
            numbers = [int(n) for n in numbers.split(" ")]
            if (is_solution(goal, numbers)):
                total += goal
    print(total)


if __name__ == "__main__":
    main()