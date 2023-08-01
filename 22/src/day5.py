from aocd import get_data
from io import StringIO
import math

input = StringIO(get_data(year=2022, day=5))

def split_crates_and_moves(input):
    crate_data = []
    move_data = []
    crates_complete = False
    for line in input:
        if not crates_complete:
            if line == '\n':
                crates_complete = True
            else:
                crate_data.append(line)
        else:
            move_data.append(line)
    return (crate_data, move_data)

def build_crate_stacks(crate_data):
    stacks = {}
    num_of_stacks = len(crate_data[0])//4
    crate_data.reverse()
    def get_index_offset(index):
        block_size = 4
        return (index * block_size) + 1
    for index in range(num_of_stacks):
        initial_row = True
        key = ''
        for row in crate_data:
            char = row[get_index_offset(index)]
            if initial_row:
                key = char
                stacks[key] = []
                initial_row = False
            elif char == ' ':
                break
            else:
                stacks[key].append(char)
    return stacks

def move_to_tuple(move_line):
    move_line = move_line.replace('\n', '')
    parts = move_line.split(' ')
    return (parts[1], parts[3], parts[5])

def compress_moves(move_data):
    moves = []
    for line in move_data:
        moves.append(move_to_tuple(line))
    return moves

def part1():
    data_chunks = split_crates_and_moves(input)
    stacks = build_crate_stacks(data_chunks[0])
    moves = compress_moves(data_chunks[1])
    for move in moves:
        count = move[0]
        for index in range(int(count)):
            stacks[move[2]].append(stacks[move[1]].pop())
    message = ''
    for key in stacks:
        message = message + stacks[key].pop()
    print(message)

def part2():
    data_chunks = split_crates_and_moves(input)
    stacks = build_crate_stacks(data_chunks[0])
    moves = compress_moves(data_chunks[1])
    for move in moves:
        count = move[0]
        temp = []
        for index in range(int(count)):
            temp.append(stacks[move[1]].pop())
        while len(temp):
            stacks[move[2]].append(temp.pop())
    message = ''
    for key in stacks:
        message = message + stacks[key].pop()
    print(message)

part2()
