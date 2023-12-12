from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2023, day=10))
testInput = [
'..F7.',
'.FJ|.',
'SJ.L7',
'|F--J',
'LJ...'
]
testInput2 = [
'.S-------7.',
'.|F-----7|.',
'.||.....||.',
'.||.....||.',
'.|L-7.F-J|.',
'.|..|.|..|.',
'.L--J.L--J.'
]
testInput3 = [
'FF7FSF7F7F7F7F7F---7',
'L|LJ||||||||||||F--J',
'FL-7LJLJ||||||LJL-77',
'F--JF--7||LJLJ7F7FJ-',
'L---JF-JLJ.||-FJLJJ7',
'|F|F-JF---7F7-L7L|7|',
'|FFJF7L7F-JF7|JL---7',
'7-L-JL7||F7|L7F-7F7|',
'L.L7LFJ|||||FJL7||LJ',
'L7JLJL-JLJLJL--JLJ.L'
]

north = 'n'
south = 's'
east = 'e'
west = 'w'
blocked = 'b'
start = 'S'
inside = 'I'

def getPipeMap(data):
    pipeMap = []
    for row in data:
        for x, symbol in enumerate(row):
            if len(pipeMap) <= x:
                pipeMap.append([])
            pipeMap[x].append(symbol)
    return pipeMap

def getNorth(coords):
    return (coords[0], coords[1]-1)
def getSouth(coords):
    return (coords[0], coords[1]+1)
def getEast(coords):
    return (coords[0]+1, coords[1])
def getWest(coords):
    return (coords[0]-1, coords[1])
def getNextCoords(direction, coords):
    if direction == north:
        return getNorth(coords)
    if direction == east:
        return getEast(coords)
    if direction == south:
        return getSouth(coords)
    return getWest(coords)

def getConnections(symbol):
    if symbol == '|':
        return (north, south)
    if symbol == '-':
        return (west, east)
    if symbol == 'L':
        return (north, east)
    if symbol == 'J':
        return (west, north)
    if symbol == '7':
        return (west, south)
    if symbol == 'F':
        return (east, south)
    return (blocked, blocked)

def getOppositeDir(direction):
    if direction == north:
        return south
    if direction == east:
        return west
    if direction == south:
        return north
    return east

def getNextDir(fromDir, symbol):
    dirs = getConnections(symbol)
    if dirs[0] == getOppositeDir(fromDir):
        return dirs[1]
    return dirs[0]

def getStartCoords(map):
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == start:
                return (x, y)

def getStartDirection(map, startCoords):
    checkLocation = getNorth(startCoords)
    checkConnections = getConnections(map[checkLocation[0]][checkLocation[1]])
    if checkConnections[0] == south or checkConnections[1] == south:
        return north
    checkLocation = getEast(startCoords)
    checkConnections = getConnections(map[checkLocation[0]][checkLocation[1]])
    if checkConnections[0] == west or checkConnections[1] == west:
        return east
    return south

def isSameLocation(coord1, coord2):
    if coord1[0] == coord2[0] and coord1[1] == coord2[1]:
        return True
    return False

def part1(data):
    pipeMap = getPipeMap(data)
    startCoords = getStartCoords(pipeMap)
    direction = getStartDirection(pipeMap, startCoords)
    coords = startCoords
    pathLengh = 0
    going = True
    while going:
        coords = getNextCoords(direction, coords)
        symbol = pipeMap[coords[0]][coords[1]]
        direction = getNextDir(direction, symbol)
        pathLengh = pathLengh + 1
        if isSameLocation(coords, startCoords):
            going = False

    print(pathLengh/2)

def isCoordInList(coord, coordList):
    for checkCoord in coordList:
        if isSameLocation(coord, checkCoord):
            return True
    return False
        
def part2(data):
    pipeMap = getPipeMap(data)
    startCoords = getStartCoords(pipeMap)
    direction = getStartDirection(pipeMap, startCoords)
    coords = startCoords
    pathCoords = []
    going = True
    while going:
        pathCoords.append(coords)
        coords = getNextCoords(direction, coords)
        symbol = pipeMap[coords[0]][coords[1]]
        direction = getNextDir(direction, symbol)
        if isSameLocation(coords, startCoords):
            going = False

    insideCount = 0
    for y in range(len(pipeMap[0])):
        crossCount = 0
        downwardLeft = False
        upwardLeft = False
        for x in range(len(pipeMap)):
            if isCoordInList((x, y), pathCoords):
                symbol = pipeMap[x][y]
                if symbol == '|':
                    crossCount = crossCount + 1
                elif symbol == 'L':
                    downwardLeft = True
                elif symbol == 'F':
                    upwardLeft = True
                elif downwardLeft and symbol == '7':
                    crossCount = crossCount + 1
                    downwardLeft = False
                elif downwardLeft and symbol == 'J':
                    downwardLeft = False
                elif upwardLeft and symbol == 'J':
                    crossCount = crossCount + 1
                    upwardLeft = False
                elif upwardLeft and symbol == '7':
                    upwardLeft = False
            elif crossCount % 2 == 1:
                insideCount = insideCount + 1
    print(insideCount)

part2(input)
