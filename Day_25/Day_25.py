#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    return

def part_1():
    locks = []
    keys = []
    total = 0
    with open("Day_25_input.txt", 'r', encoding="utf-8") as file:
        shematics = file.read().split('\n\n')
        for shematic in shematics:
            ligns = shematic.strip().split("\n")
            values = [-1, -1, -1, -1, -1]
            for lign in ligns:
                for i in range(5):
                    if lign[i] == '#':
                        values[i] += 1
            if (ligns[0] == "#####"):
                locks.append(values)
            else:
                keys.append(values)
    for key in keys:
        for lock in locks:
            valid = True
            for i in range(5):
                if (lock[i] + key[i] > 5):
                    valid = False
            if (valid == True):
                total += 1
    print(total)


if __name__ == "__main__":
    main()