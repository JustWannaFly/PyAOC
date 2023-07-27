from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2022, day=3))

def get_prio(item):
    items = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return items.index(item)

def part1():
    total = 0
    for line in input:
        line = line.replace('\n', '')
        midpoint = int(line.__len__()/2)
        pocket1 = line[:midpoint]
        pocket2 = line[midpoint:]
        common = set(pocket1).intersection(pocket2)
        while common.__len__() > 0:
            total += get_prio(common.pop())
    print(total)

def part2():
    total = 0
    pack1 = ''
    pack2 = ''
    for line in input:
        line = line.replace('\n', '')
        if (pack1 == ''): 
            pack1 = line
        elif (pack2 == ''):
            pack2 = line
        else:
            common = set(pack1).intersection(pack2).intersection(line)
            total += get_prio(common.pop())
            pack1 = ''
            pack2 = ''
    print(total)
part2()
