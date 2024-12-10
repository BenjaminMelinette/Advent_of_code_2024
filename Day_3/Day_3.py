#!/usr/bin/python3

import re

def main():
    part_1()
    part_2()


def part_2():
    total = 0
    with open("Day_3_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            # Séparer la ligne sur "don't()"
            data_v1 = line.split("don't()")
            
            for i in range(len(data_v1)):
                if i != 0:
                    # Séparer à nouveau sur "do()"
                    data_v2 = data_v1[i].split("do()")
                    # Si des éléments sont présents, traiter ceux après "do()"
                    if len(data_v2) > 1:
                        data_v2 = data_v2[1:]  # Enlever la première partie, qui est vide
                    else:
                        data_v2 = []
                else:
                    data_v2 = [data_v1[0]]

                # Parcourir chaque morceau pour chercher des expressions
                for do in data_v2:
                    expressions = extract_expression_mul(do)
                    for elem in expressions:
                        total += elem[0] * elem[1]
    
    print(f"Total part 2: {total}")


def extract_expression_mul(text):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, text)
    results = [(int(x), int(y)) for x, y in matches]
    return results

def part_1():
    total = 0
    with open("Day_3_input.txt", 'r', encoding="utf-8") as file:
        for line in file:
            expressions = extract_expression_mul(line)
            for elem in expressions:
                total += elem[0] * elem[1]
    print(total)


if __name__ == "__main__":
    main()