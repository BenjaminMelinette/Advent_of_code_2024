#!/usr/bin/python3

from collections import defaultdict

def main():
    part_1()
    part_2()

def part_2():
    prices = []
    with open("Day_22_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            secret = int(line.strip())
            price = []
            for _ in range(2000):
                secret = ((secret * 64) ^ secret) % 16777216
                secret = ((secret // 32) ^ secret) % 16777216
                secret = ((secret * 2048) ^ secret) % 16777216
                price.append(secret % 10)
            prices.append(price)
    changes = [[b - a for a, b in zip(p, p[1:])] for p in prices]

    amounts = defaultdict(int)
    for buyer_idx, change in enumerate(changes):
        keys = set()
        for i in range(len(change) - 3):
            key = tuple(change[i : i + 4])
            if key in keys:
                continue
            amounts[key] += prices[buyer_idx][i + 4]
            keys.add(key)
    max_amount = max(amounts.values())

    print(max_amount)

def part_1():
    results = []
    with open("Day_22_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            secret = int(line.strip())
            for _ in range(2000):
                secret = ((secret * 64) ^ secret) % 16777216
                secret = ((secret // 32) ^ secret) % 16777216
                secret = ((secret * 2048) ^ secret) % 16777216
            results.append(secret)
    print(sum(results))

if __name__ == "__main__":
    main()