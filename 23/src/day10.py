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

north = 'n'
south = 's'
east = 'e'
west = 'w'
blocked = 'b'
start = 'S'

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

def part2(data):
    print('I dunno yet')

part1(input)
