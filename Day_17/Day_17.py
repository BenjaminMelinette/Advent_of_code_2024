#!/usr/bin/python3

def main():
    part_1()
    part_2()

def part_2():
    with open("Day_17_input.txt", 'r', encoding="utf-8") as file:
        content = file.read().split("\n\n")
        registers = [
            0,
            int(content[0].strip().split("\n")[1].split(": ")[1]),
            int(content[0].strip().split("\n")[2].split(": ")[1])
        ]
        program = list(map(int, content[1].strip().split(": ")[1].split(",")))
    registers[0] = sum(7 * 8**i for i in range(len(program) - 1)) + 1
    result = run(registers, program)
    while result != program:
        add = 0
        for i in range(len(result) - 1, -1, -1):
            if result[i] != program[i]:
                add = 8**i
                registers[0] += add
                break
        result = run(registers, program)
    print(registers[0])


def combo_operand(operand, registers):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers[0]
        case 5:
            return registers[1]
        case 6:
            return registers[2]

def run(registers, program):
    pointer = 0
    A, B, C = registers
    outputs = []

    while pointer < len(program):
        instruction = program[pointer]
        operand = program[pointer + 1]

        if instruction == 0:  # adv
            A //= 2 ** combo_operand(operand, [A, B, C])
        elif instruction == 1:  # bxl
            B ^= operand
        elif instruction == 2:  # bst
            B = combo_operand(operand, [A, B, C]) % 8
        elif instruction == 3:  # jnz
            if A != 0:
                pointer = operand
                continue
        elif instruction == 4:  # bxc
            B ^= C
        elif instruction == 5:  # out
            outputs.append(combo_operand(operand, [A, B, C]) % 8)
        elif instruction == 6:  # bdv
            B = A // (2 ** combo_operand(operand, [A, B, C]))
        elif instruction == 7:  # cdv
            C = A // (2 ** combo_operand(operand, [A, B, C]))
            
        pointer += 2
    return outputs

def part_1():
    with open("Day_17_input.txt", 'r', encoding="utf-8") as file:
        content = file.read().split("\n\n")
        registers = [
            int(content[0].strip().split("\n")[0].split(": ")[1]),
            int(content[0].strip().split("\n")[1].split(": ")[1]),
            int(content[0].strip().split("\n")[2].split(": ")[1])
        ]
        program = list(map(int, content[1].strip().split(": ")[1].split(",")))
    print(registers, program)
    print(run(registers, program))



if __name__ == "__main__":
    main()