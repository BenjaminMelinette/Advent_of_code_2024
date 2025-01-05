#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    return

DP = {}

def match(goal, patterns):
    if goal in DP:
        return DP[goal]
    ans = 0
    if not goal:
        ans = 1
    for pattern in patterns:
        if goal.startswith(pattern):
            ans += match(goal[len(pattern):], patterns)
    DP[goal] = ans
    return ans

def part_1():
    patterns = []
    words = []
    total = 0
    total_2 = 0
    with open("Day_19_input.txt", 'r', encoding="utf-8") as file:
        part = file.read().split("\n\n")
        patterns = part[0].strip().split(', ')
        words = part[1].strip().split('\n')
    for word in words:
        res = match(word, patterns)
        if res > 0:
            total += 1
        total_2 += res
    print(total)
    print(total_2)
    


if __name__ == "__main__":
    main()