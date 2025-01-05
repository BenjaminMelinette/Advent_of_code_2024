#!/usr/bin/python3

class Region:
    DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def __init__(self, tiles, sign):
        self.tiles = tiles
        self.sign = sign
        self.side_visited = set()

    def area(self):
        return len(self.tiles)

    def perimeter(self, map):
        tot = 0
        for tile in self.tiles:
            for d in self.DIRECTIONS:
                ni, nj = tile[0] + d[0], tile[1] + d[1]
                if not (0 <= ni < len(map) and 0 <= nj < len(map[0]) and map[ni][nj] == self.sign):
                    tot += 1
        return tot

def find_all_region(tile, map, used):
    directions = Region.DIRECTIONS
    region = []
    stack = [tile]

    while stack:
        t = stack.pop()
        if t not in used:
            used.add(t)
            region.append(t)
            for d in directions:
                ni, nj = t[0] + d[0], t[1] + d[1]
                if (0 <= ni < len(map) and 0 <= nj < len(map[0]) and
                        map[ni][nj] == map[t[0]][t[1]]):
                    stack.append((ni, nj))
    return region

def find_new_regions(map, used):
    regions = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (i, j) not in used:
                tiles = find_all_region((i, j), map, used)
                if tiles:
                    regions.append(Region(tiles, map[i][j]))
    return regions

def part_1():
    map = []
    with open("Day_12_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            map.append(list(line.strip()))

    used = set()
    regions = find_new_regions(map, used)

    total_price = sum(region.area() * region.perimeter(map) for region in regions)
    print("Total price of fencing all regions:", total_price)

def main():
    part_1()
    part_2()

def calculate_sides(region, map):
    min_y = min(region.tiles, key=lambda x: x[0])[0]
    max_y = max(region.tiles, key=lambda x: x[0])[0]
    min_x = min(region.tiles, key=lambda x: x[1])[1]
    max_x = max(region.tiles, key=lambda x: x[1])[1]
    rows = max_y - min_y + 1
    cols = max_x - min_x + 1
    new_group = [(y - min_y, x - min_x) for y, x in region.tiles]

    grid = [[" " for _ in range(cols + 2)] for _ in range(rows + 2)]
    for y, x in new_group:
        grid[y + 1][x + 1] = "X"

    sides = 0

    for _ in range(2):
        for y in range(1, rows + 1):
            sides += len("".join(["X" if current != above and current == "X" else " " for current, above in zip(grid[y], grid[y - 1])]).split())
            sides += len("".join(["X" if current != below and current == "X" else " " for current, below in zip(grid[y], grid[y + 1])]).split())

        grid = list(zip(*grid[::-1]))
        rows, cols = cols, rows

    return sides

def part_2():
    map = []
    with open("Day_12_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            map.append(list(line.strip()))

    used = set()
    regions = find_new_regions(map, used)

    total_price = 0
    for region in regions:
        sides = calculate_sides(region, map)
        print(region.tiles, region.sign, sides)
        price = region.area() * sides
        total_price += price

    print("Total price of fencing all regions (Part 2):", total_price)


def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()
