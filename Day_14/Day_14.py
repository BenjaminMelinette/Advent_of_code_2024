#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    return

def part_1():
    robots = []
    with open("Day_14_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            a, b = line.split(" ")
            x, y = map(int, a[2:].split(","))
            vx, vy = map(int, b[2:].split(","))
            robots.append(((x, y), (vx, vy)))
    width = 101
    height = 103
    quadrants = [0, 0, 0 ,0]
    for robot in robots:
        (x, y), (vx, vy) = robot
        for i in range(100):
            x = (x + vx) % width
            y = (y + vy) % height
        if x == width // 2 or y == height // 2:
                continue
        index = (int(x > width // 2)) + (int(y > height // 2) * 2)
        quadrants[index] += 1
    print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

if __name__ == "__main__":
    main()