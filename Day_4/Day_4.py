#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    total = 0
    tab = []
    with open("Day_4_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            tab.append(line.strip())
    
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if check_xmas(i, j, tab):
                total += 1

    print(total)

def check_xmas(x, y, tab):
    rows, cols = len(tab), len(tab[0])
    
    if not (0 <= x - 1 < rows and 0 <= y - 1 < cols and
            0 <= x + 1 < rows and 0 <= y + 1 < cols):
        return False

    if tab[x - 1][y - 1] == 'M' and tab[x][y] == 'A' and tab[x + 1][y + 1] == 'S':
        if tab[x - 1][y + 1] == 'S' and tab[x][y] == 'A' and tab[x + 1][y - 1] == 'M':
            return True

    if tab[x - 1][y - 1] == 'S' and tab[x][y] == 'A' and tab[x + 1][y + 1] == 'M':
        if tab[x - 1][y + 1] == 'M' and tab[x][y] == 'A' and tab[x + 1][y - 1] == 'S':
            return True

    if tab[x - 1][y - 1] == 'M' and tab[x][y] == 'A' and tab[x + 1][y + 1] == 'S':
        if tab[x - 1][y + 1] == 'M' and tab[x][y] == 'A' and tab[x + 1][y - 1] == 'S':
            return True

    if tab[x - 1][y - 1] == 'S' and tab[x][y] == 'A' and tab[x + 1][y + 1] == 'M':
        if tab[x - 1][y + 1] == 'S' and tab[x][y] == 'A' and tab[x + 1][y - 1] == 'M':
            return True

    return False

def check_word(x, y, tab, word, dx, dy):
    if not (0 <= x + dx * (len(word) - 1) < len(tab)) or not (0 <= y + dy * (len(word) - 1) < len(tab[0])):
        return False
    for i in range(len(word)):
        if tab[x + i * dx][y + i * dy] != word[i]:
            return False
    return True

def part_1():
    total = 0
    word = "XMAS"
    tab = []
    with open("Day_4_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            tab.append(line.strip())

    directions = [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0), (0, -1)]

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            for dx, dy in directions:
                if check_word(i, j, tab, word, dx, dy):
                    total += 1
    print(total)


if __name__ == "__main__":
    main()