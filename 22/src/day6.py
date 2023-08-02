from aocd import get_data

input = get_data(year=2022, day=6)

def part1():
    for index in range(3, len(input)):
        uniques = len({input[index], input[index - 1], input[index - 2], input[index - 3]})
        if uniques == 4:
            print(index + 1)
            return
        
def part2():
    for index in range(3, len(input)):
        unique_length = 14
        chars = set()
        for inner in range(unique_length):
            chars.add(input[index - inner])
        if len(chars) == unique_length:
            print(index + 1)
            return

part2()
