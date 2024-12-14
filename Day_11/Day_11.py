#!/usr/bin/python3

from collections import Counter

def main():
    part_1()
    part_2()

def simulate_blink_optimized(stones_count):
    new_stones_count = Counter()
    for stone, count in stones_count.items():
        if stone == "0":
            new_stones_count["1"] += count
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            left = stone[:mid]
            right = str(int(stone[mid:]))
            new_stones_count[left] += count
            new_stones_count[right] += count
        else:
            new_stones_count[str(int(stone) * 2024)] += count
    return new_stones_count

def part_2():
    stones_count = Counter()
    with open("Day_11_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            stones = line.strip().split(" ")
            for stone in stones:
                stones_count[stone] += 1
    for i in range(75):
        stones_count = simulate_blink_optimized(stones_count)
    total_stones = sum(stones_count.values())
    print(total_stones)

def simulate_blink(stones):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            new_stones.append(stone[:mid])
            new_stones.append(str(int(stone[mid:])))
        else:
            new_stones.append(str(int(stone) * 2024))
    return new_stones

def part_1():
    stones = []
    with open("Day_11_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            stones = line.strip().split(" ")
    for i in range(25):
        stones = simulate_blink(stones)
    print(len(stones))
    
    

if __name__ == "__main__":
    main()