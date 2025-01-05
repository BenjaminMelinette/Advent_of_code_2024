#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    input_data = []
    map_input = []
    with open("Day_18_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            input_data.append([*map(int, line.split(","))])
    map_input = create_map(input_data)
    for i in range(1024, len(input_data), 1):
        x, y = input_data[i]
        map_input[x][y] = '#'
        if find_shortest(map_input) == -1:
            print(x, y)
            return

def create_map(input_data):
    map_input = [["."] * 71 for _ in range(71)]
    i = 0
    for x, y in input_data:
        if (i >= 1024):
            return map_input
        map_input[x][y] = "#"
        i += 1

def find_shortest(map_input):
    queue = [((0, 0), 0)]
    seen = set()
    while queue:
        pos, length = queue.pop(0)
        if pos == (70, 70):
            return length
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and map_input[ny][nx] == ".":
                queue.append(((nx, ny), length + 1))
    return -1

def part_1():
    input_data = []
    map_input = []
    with open("Day_18_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            input_data.append([*map(int, line.split(","))])
    map_input = create_map(input_data)
    print(find_shortest(map_input))



if __name__ == "__main__":
    main()