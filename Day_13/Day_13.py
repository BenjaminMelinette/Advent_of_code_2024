#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    with open("Day_13_input.txt", 'r', encoding="utf-8") as file:
        machines = (file.read().split('\n\n'))
    coins = 0
    for machine in machines:
        btn_a, btn_b, prize = machine.split('\n')
        btn_a_x = int(btn_a.split(",")[0].split('X')[1])
        btn_a_y = int(btn_a.split(",")[1].split('Y')[1])
        btn_b_x = int(btn_b.split(",")[0].split('X')[1])
        btn_b_y = int(btn_b.split(",")[1].split('Y')[1])
        price_x = int(prize.split(",")[0].split("=")[1]) + 10000000000000
        price_y = int(prize.split(",")[1].split("=")[1]) + 10000000000000

        # Règle Cramer
        times_btn_b_pressed = (price_y * btn_a_x - price_x * btn_a_y) / (btn_b_y * btn_a_x - btn_b_x * btn_a_y)
        times_btn_a_pressed = (price_x - btn_b_x * times_btn_b_pressed) / btn_a_x

        if times_btn_a_pressed.is_integer() and times_btn_b_pressed.is_integer():
            coins += int(times_btn_a_pressed) * 3 + int(times_btn_b_pressed)

    print(f"Part 2 : {coins}")

def part_1():
    with open("Day_13_input.txt", 'r', encoding="utf-8") as file:
        machines = (file.read().split('\n\n'))
    coins = 0
    for machine in machines:
        btn_a, btn_b, prize = machine.split('\n')
        btn_a_x = int(btn_a.split(",")[0].split('X')[1])
        btn_a_y = int(btn_a.split(",")[1].split('Y')[1])
        btn_b_x = int(btn_b.split(",")[0].split('X')[1])
        btn_b_y = int(btn_b.split(",")[1].split('Y')[1])
        price_x = int(prize.split(",")[0].split("=")[1])
        price_y = int(prize.split(",")[1].split("=")[1])

        # Règle Cramer
        times_btn_b_pressed = (price_y * btn_a_x - price_x * btn_a_y) / (btn_b_y * btn_a_x - btn_b_x * btn_a_y)
        times_btn_a_pressed = (price_x - btn_b_x * times_btn_b_pressed) / btn_a_x

        if 100 >= times_btn_a_pressed >= 0 and 100 >= times_btn_b_pressed >= 0 and times_btn_a_pressed.is_integer() and times_btn_b_pressed.is_integer():
                coins += int(times_btn_a_pressed) * 3 + int(times_btn_b_pressed)

    print(coins)

if __name__ == "__main__":
    main()