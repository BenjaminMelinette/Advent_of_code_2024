#!/usr/bin/python3

def main():
    part_1()
    part_2()

def check_level(level):
    up = False
    down = False
    if (level[0] > level[1]):
        down = True
    else:
        up = True
    for i in range(len(level) - 1):
        if (up and level[i] > level[i + 1]):
            return False
        if (down and level[i] < level[i + 1]):
            return False
        if (level[i] == level[i + 1]):
            return False
        if (abs(level[i] - level[i + 1]) > 3):
            return False
    return True

def check_level_p2(level):
    for i in range(len(level)):
        level_copy = level[:i] + level[i + 1:]
        if check_level(level_copy):
            return True
    return False


def part_1():
    levels = []
    safe = 0
    with open("Day_2_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            res = line.split(" ")
            res[-1] = res[-1].rstrip("\n")
            for i in range(len(res)):
                res[i] = int(res[i])
            levels.append(res)
    for level in levels:
        if (check_level(level)):
            safe += 1
    print(safe)

def part_2():
    levels = []
    safe = 0
    with open("Day_2_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            res = line.split(" ")
            res[-1] = res[-1].rstrip("\n")
            for i in range(len(res)):
                res[i] = int(res[i])
            levels.append(res)
    for level in levels:
        if (check_level_p2(level)):
            safe += 1
    print(safe)
    return

if __name__ == "__main__":
    main()