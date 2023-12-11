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
part2Test = [
'LR',
'',
'11A = (11B, XXX)',
'11B = (XXX, 11Z)',
'11Z = (11B, XXX)',
'22A = (22B, XXX)',
'22B = (22C, 22C)',
'22C = (22Z, 22Z)',
'22Z = (22B, 22B)',
'XXX = (XXX, XXX)'
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

def allEndInZ(locations):
    for loc in locations:
        if not loc[len(loc)-1] == 'Z':
            return False
    return True

def getStartingLocations(desertMap):
    locations = []
    for key in desertMap.keys():
        if key[len(key)-1] == 'A':
            locations.append(key)
    return locations


def part2(data):
    directions, desertMap = parseInput(data)
    locations = getStartingLocations(desertMap)
    steps = 0
    while not allEndInZ(locations):
        direction = directions[steps % len(directions)]
        steps = steps + 1
        targetIndex = 0
        if direction == 'R':
            targetIndex = 1
        newLocations = []
        for location in locations:
            newLocations.append(desertMap[location][targetIndex])
        locations = newLocations

    print('steps taken: ' + str(steps))

part2(input)
