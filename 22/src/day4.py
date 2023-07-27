from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2022, day=4))

def parse_elfs(line):
    str_elfs = line.split(',')
    elfs = []
    for str in str_elfs:
        bounds = str.split('-')
        elfs.append((int(bounds[0]), int(bounds[1])))
    return elfs

def part1():
    count = 0
    for line in input:
        line = line.replace('\n', '')
        elfs = parse_elfs(line)
        if (elfs[0][0] >= elfs[1][0] and elfs[0][1] <= elfs[1][1] or 
            elfs[1][0] >= elfs[0][0] and elfs[1][1] <= elfs[0][1]):
            count += 1
    print(count)

def part2():
    count = 0
    for line in input:
        line = line.replace('\n', '')
        elfs = parse_elfs(line)
        if (elfs[0][0] <= elfs[1][1] and elfs[1][0] <= elfs[0][0] or
                elfs[0][1] >= elfs[1][1] and elfs[1][1] >= elfs[0][1] or
                elfs[1][0] <= elfs[0][1] and elfs[0][0] <= elfs[1][0] or
                elfs[1][1] >= elfs[0][1] and elfs[0][1] >= elfs[1][1]):
            count += 1
    print(count)

part2()