#!/usr/bin/python3

class Block:
    def __init__(self, space_length, files=None):
        if files is None:
            files = []
        self.space_length = space_length
        self.files = files
        if files:
            self.space_length = 0

    def add_file(self, file_id, length):
        space_used = 0
        if (length == 0):
            return 0
        if (length > self.space_length):
            space_used = self.space_length
        else:
            space_used = length
        
        self.files.append((file_id, space_used))
        self.space_length -= space_used
        return length - space_used

    def get_checksum(self, id_start):
        res = 0
        index = 0
        for file_id, size in self.files:
            for i in range(size):
                res += file_id * (id_start + i + index)
            index += size
        return (res, id_start + index)

    def get_complete_block_size(self):
        i = 0
        total_size = 0
        for file_id, size in self.files:
            total_size += size

    def get_size_used(self):
        res = 0
        for file_id, size in self.files:
            res += size
        return res

def main():
    part_1()
    part_2()


def part_2():
    blocks = []
    space_idx = []
    
    with open("Day_9_input.txt", 'r', encoding="utf-8") as file:
        disk_representation = file.read().strip()

    for i, char in enumerate(disk_representation):
        if i % 2 == 0:
            blocks.append(Block(
                int(char), 
                [(i // 2, int(char))]
            ))
        else:
            blocks.append(Block(int(char)))
            space_idx.append(len(blocks) - 1)

    curr_block_idx = len(blocks) - 1

    while curr_block_idx > 0:
        curr_block = blocks[curr_block_idx]

        if curr_block.space_length > 0:
            curr_block_idx -= 1
            continue

        curr_block_len = curr_block.get_size_used()

        for space in space_idx:
            if space >= curr_block_idx:
                break

            if blocks[space].space_length >= curr_block_len:
                blocks[space].files.extend(curr_block.files)
                blocks[space].space_length -= curr_block_len

                curr_block.files = []
                curr_block.space_length = curr_block_len

                if blocks[space].space_length == 0:
                    space_idx.remove(space)

                break

        curr_block_idx -= 1

    checksum = 0
    pos = 0

    for block in blocks:
        for file_id, size in block.files:
            for _ in range(size):
                checksum += file_id * pos
                pos += 1
        pos += block.space_length

    print(f"Final checksum: {checksum}")



def space_left(blocks):
    for i, block in enumerate(blocks):
        if block.space_length != 0:
            return i
    return -1

def space_left_minimum(blocks, min):
    for i, block in enumerate(blocks):
        if block.space_length >= min:
            return i
    return -1

def part_1():
    blocks = []
    res = 0
    block_id = 0

    # Lire et analyser le fichier
    with open("Day_9_input.txt", 'r', encoding="utf-8") as file:
        disk_representation = file.read().strip()

    # Création des blocs
    for i in range(len(disk_representation)):
        if i % 2 == 0:
            blocks.append(Block(
                int(disk_representation[i]), 
                [(i // 2, int(disk_representation[i]))]
            ))
        else:
            blocks.append(Block(int(disk_representation[i])))

    block_space_left = space_left(blocks)
    while block_space_left != -1:
        print(f"Iteration start - Block space left: {block_space_left}")
        block_to_move = blocks[-1]

        if not block_to_move.files:
            print(f"Removing empty block at index {len(blocks) - 1}")
            blocks.pop()
            block_space_left = space_left(blocks)
            continue

        file_to_move = block_to_move.files.pop(0)
        file_id, file_length = file_to_move
        print(f"Moving file {file_id} from block {len(blocks) - 1}, size: {file_length}")
        
        block_left_to_move = blocks[block_space_left].add_file(file_id, file_length)

        while block_left_to_move > 0:
            block_space_left = space_left(blocks)
            if block_space_left == -1:
                print("No space left to move files. Exiting...")
                break
            block_left_to_move = blocks[block_space_left].add_file(file_id, block_left_to_move)

        print(f"File moved. Remaining length to move: {block_left_to_move}")

        if block_left_to_move > 0:
            block_to_move.files.insert(0, (file_id, block_left_to_move))

        block_space_left = space_left(blocks)

    for block in blocks:
        checksum, new_id = block.get_checksum(block_id)
        block_id = new_id
        res += checksum
    print(res)



    


if __name__ == "__main__":
    main()