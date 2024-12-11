#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    return

def part_1():
    disk_representation = ""
    with open("Day_9_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            disk = line.strip("")
        for i in range(len(disk)):
            if (i % 2 == 0):
                disk_representation += f'{int(i / 2)}' * int(disk[i])
            else:
                disk_representation += '.' * int(disk[i])
    

if __name__ == "__main__":
    main()