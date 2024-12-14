#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    tab = []
    trailheads = []
    ends = {}
    res = 0
    with open("Day_10_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            tab.append(line.strip())
        trailheads, ends = find_edge(tab)
    for trailhead in trailheads:
        explore_path(tab, trailhead, trailhead, ends)
    for end, paths in ends.items():
        res += len(paths)
    print(res)

def find_edge(tab):
    trailheads = []
    ends = {}
    for x in range(len(tab)):
        for y in range(len(tab[x])):
            if (tab[x][y] == '0'):
                trailheads.append((x, y))
            if (tab[x][y] == '9'):
                ends[(x, y)] = []
    return trailheads, ends
            
def explore_path_no_double(tab, start_pos, current_pos, ends):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    height = int(tab[current_pos[0]][current_pos[1]])

    for dx, dy in directions:
        new_x, new_y = current_pos[0] + dx, current_pos[1] + dy

        if 0 <= new_x < len(tab) and 0 <= new_y < len(tab[0]):
            next_height = tab[new_x][new_y]

            if next_height == str(height + 1):
                if next_height == '9':
                    if start_pos not in ends[(new_x, new_y)]:
                        ends[(new_x, new_y)].append(start_pos)
                else:
                    explore_path_no_double(tab, start_pos, (new_x, new_y), ends)
    return

def explore_path(tab, start_pos, current_pos, ends):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    height = int(tab[current_pos[0]][current_pos[1]])

    for dx, dy in directions:
        new_x, new_y = current_pos[0] + dx, current_pos[1] + dy

        if 0 <= new_x < len(tab) and 0 <= new_y < len(tab[0]):
            next_height = tab[new_x][new_y]

            if next_height == str(height + 1):
                if next_height == '9':
                    ends[(new_x, new_y)].append(start_pos)
                else:
                    explore_path(tab, start_pos, (new_x, new_y), ends)
    return

def part_1():
    tab = []
    trailheads = []
    ends = {}
    res = 0
    with open("Day_10_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            tab.append(line.strip())
        trailheads, ends = find_edge(tab)
    for trailhead in trailheads:
        explore_path_no_double(tab, trailhead, trailhead, ends)
    for end, paths in ends.items():
        res += len(paths)
    print(res)
        


if __name__ == "__main__":
    main()