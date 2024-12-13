#!/usr/bin/python3
from collections import defaultdict

def main():
    part_1()
    part_2()

def part_2():
    tab = []
    with open("Day_8_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            tab.append(line.strip())
            
    antennas = defaultdict(list)
    for row in range(len(tab)):
        for col in range(len(tab[0])):
            if tab[row][col] != ".":
                antennas[tab[row][col]].append((row, col))
    
    antinodes = set()

    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords), 1):
                diff = (coords[j][0] - coords[i][0] , coords[j][1] - coords[i][1])
                diff_i = (diff[0] * (-1), diff[1] * (-1))
                new_pos_i = (coords[i][0] + diff_i[0] , coords[i][1] + diff_i[1])
                new_pos_j = (coords[j][0] + diff[0] , coords[j][1] + diff[1])

                while (0 <= new_pos_i[0] < len(tab) and 0 <= new_pos_i[1] < len(tab[0])):
                    antinodes.add(new_pos_i)
                    new_pos_i = (new_pos_i[0] + diff_i[0] , new_pos_i[1] + diff_i[1])

                while (0 <= new_pos_j[0] < len(tab) and 0 <= new_pos_j[1] < len(tab[0])):
                    antinodes.add(new_pos_j)
                    new_pos_j = (new_pos_j[0] + diff[0] , new_pos_j[1] + diff[1])

                antinodes.add(coords[i])
                antinodes.add(coords[j])
    print(len(antinodes))
    return

def part_1():
    tab = []
    with open("Day_8_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            tab.append(line.strip())
            
    antennas = defaultdict(list)
    for row in range(len(tab)):
        for col in range(len(tab[0])):
            if tab[row][col] != ".":
                antennas[tab[row][col]].append((row, col))
    
    antinodes = set()

    for antenna, coords in antennas.items():
        for i in range(len(coords)):
            for j in range(i + 1, len(coords), 1):
                diff = (coords[j][0] - coords[i][0] , coords[j][1] - coords[i][1])
                diff_i = (diff[0] * (-1), diff[1] * (-1))

                if (0 <= coords[i][0] + diff_i[0] < len(tab)):
                    if (0 <= coords[i][1] + diff_i[1] < len(tab[0])):
                        antinodes.add((coords[i][0] + diff_i[0], coords[i][1] + diff_i[1]))

                if (0 <= coords[j][0] + diff[0] < len(tab)):
                    if (0 <= coords[j][1] + diff[1] < len(tab[0])):
                        antinodes.add((coords[j][0] + diff[0], coords[j][1] + diff[1]))
    print(len(antinodes))


if __name__ == "__main__":
    main()