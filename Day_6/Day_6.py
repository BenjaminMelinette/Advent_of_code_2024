#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    map_list = []
    facing = 0
    possibility = []
    with open("Day_6_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            map_list.append(line.strip())
    pos = find_player(map_list)
    for i in range(len(map_list)):
        for j in range(len(map_list)):
            if (i, j) != pos and map_list[i][j] != '#':
                test_map = [list(row) for row in map_list]
                test_map[i][j] = 'O'
                if is_stuck_in_loop(test_map, pos):
                    possibility.append((i, j))
    print(len(possibility))

def is_stuck_in_loop(map_list, pos):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    box_visited = set()
    facing = 0
    start = pos
    count = 0
    while True:
        new_pos, new_facing = next_turn(map_list, pos, facing, "#O")
        if facing != new_facing:
            new_box = ((pos[0] + directions[facing][0]), (pos[1] + directions[facing][1]))
            if new_box in box_visited:
                count += 1
            else:
                box_visited.add(new_box)
            facing = new_facing
        pos = new_pos
        if count == 4:
            return True
        if pos == (-1, -1):
            return False

def find_player(map_list):
    for x in range(len(map_list)):
        for y in range(len(map_list[x])):
            if map_list[x][y] == '^':
                return (x, y)

def next_turn(map_list, pos, facing, obstacles="#"):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    new_pos = (pos[0] + directions[facing][0], pos[1] + directions[facing][1])
    
    if (new_pos[0] < 0 or new_pos[0] >= len(map_list) or
        new_pos[1] < 0 or new_pos[1] >= len(map_list[0])):
        return (-1, -1), facing
    elif (map_list[new_pos[0]][new_pos[1]] in obstacles):
        facing = (facing + 1) % 4
        return pos, facing
    else:
        return new_pos, facing

def part_1():
    map_list = []
    facing = 0
    visited = []
    with open("Day_6_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            map_list.append(line.strip())
    pos = find_player(map_list)
    while pos != (-1, -1):
        if (pos not in visited):
            visited.append(pos)
        pos, facing = next_turn(map_list, pos, facing)
    print(len(visited))


if __name__ == "__main__":
    main()