from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2023, day=8))
testInput = [
'LLR',
'',
'AAA = (BBB, BBB)',
'BBB = (AAA, ZZZ)',
'ZZZ = (ZZZ, ZZZ)'
]

def parseInput(data):
    desertMap = {}
    directions = None
    for line in data:
        line = line.replace('\n', '')
        if directions == None:
            directions = line
        elif ' = ' in line:
            parts = line.split(' = ')
            coordParts = parts[1].split(', ')
            desertMap[parts[0]] = (coordParts[0].replace('(', ''), coordParts[1].replace(')', ''))
    return (directions, desertMap)

def part1(data):
    location = 'AAA'
    goal = 'ZZZ'
    directions, desertMap = parseInput(data)
    steps = 0
    while not location == goal:
        direction = directions[steps % len(directions)]
        steps = steps + 1
        targetIndex = 0
        if direction == 'R':
            targetIndex = 1
        location = desertMap[location][targetIndex]

    print('steps taken: ' + str(steps))

def part2(data):
    print('I dunno yet')

part1(input)
