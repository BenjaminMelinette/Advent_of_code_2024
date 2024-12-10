#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    left_column = []
    right_column = []
    total = 0
    with open("Day_1_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            res = line.split("   ")
            left_column.append(int(res[0]))
            right_column.append(int(res[1].rstrip('\n')))
    for i in range(len(left_column)):
        total += right_column.count(left_column[i]) * left_column[i]
    print(f"Part 2 : {total}")

def part_1():
    left_column = []
    right_column = []
    total = 0
    with open("Day_1_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            res = line.split("   ")
            left_column.append(int(res[0]))
            right_column.append(int(res[1].rstrip('\n')))
    for i in range(len(left_column)):
        index_left = min(enumerate(left_column), key=lambda x: x[1])[0]
        index_right = min(enumerate(right_column), key=lambda x: x[1])[0]
        total += abs(right_column[index_right] - left_column[index_left])
        del left_column[index_left]
        del right_column[index_right]
    print(total)


if __name__ == "__main__":
    main()