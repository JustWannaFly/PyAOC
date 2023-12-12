from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2023, day=11))
testInput = [
'...#......',
'.......#..',
'#.........',
'..........',
'......#...',
'.#........',
'.........#',
'..........',
'.......#..',
'#...#.....'
]

space = '.'
galaxy = '#'

def parseInput(inputData):
    mappedData = []
    for line in inputData:
        line = line.replace('\n', '')
        mappedData.append(line)
    return mappedData

def getExpandCols(spaceMap):
    emptyCols = []
    for char in spaceMap[0]:
        emptyCols.append(True)
    for line in spaceMap:
        for idx, char in enumerate(line):
            if char == galaxy:
                emptyCols[idx] = False
    emptyList = []
    for i, isEmpty in enumerate(emptyCols):
        if isEmpty:
            emptyList.append(i)
    return emptyList

def getExpandRows(spaceMap):
    emptyRows = []
    for i, line in enumerate(spaceMap):
        isEmpty = True
        for char in line:
            if char == galaxy:
                isEmpty = False
        if isEmpty:
            emptyRows.append(i)
    return emptyRows

def expandMap(spaceMap):
    
    # expand columns
    expandedCols = []
    emptyCols = []
    for char in spaceMap[0]:
        emptyCols.append(True)
    for line in spaceMap:
        for idx, char in enumerate(line):
            if char == galaxy:
                emptyCols[idx] = False
    for line in spaceMap:
        expandedLine = ''
        for idx, char in enumerate(line):
            if emptyCols[idx]:
                expandedLine = expandedLine + '.'
            expandedLine = expandedLine + char
        expandedCols.append(expandedLine)
    
    # expand rows
    expandedMap = []
    for line in expandedCols:
        isEmpty = True
        for char in line:
            if char == galaxy:
                isEmpty = False
        expandedMap.append(line)
        if isEmpty:
            expandedMap.append(line)
    return expandedMap
    
def getGalaxyLocations(spaceMap):
    galaxyCoords = []
    for y, line in enumerate(spaceMap):
        for x, char in enumerate(line):
            if char == galaxy:
                galaxyCoords.append((x, y))
    return galaxyCoords

def part1(inputData):
    expandedData = expandMap(parseInput(inputData))
    galaxyCoords = getGalaxyLocations(expandedData)

    galaxyCount = len(galaxyCoords)
    totalDist = 0
    for i in range(galaxyCount - 1):
        remainingGalaxies = galaxyCoords[i + 1:]
        startCoord = galaxyCoords[i]
        for endCoord in remainingGalaxies:
            totalDist = totalDist + abs(startCoord[0] - endCoord[0])
            totalDist = totalDist + abs(startCoord[1] - endCoord[1])

    print(totalDist)

def getExpandCrossCount(check1, check2, expandList):
    crossCount = 0
    for entry in expandList:
        if check1 < entry and entry < check2:
            crossCount = crossCount + 1
        elif check2 < entry and entry < check1:
            crossCount = crossCount + 1
    return crossCount

def part2(data):
    spaceMap = parseInput(data)
    galaxyCoords = getGalaxyLocations(spaceMap)
    expandCols = getExpandCols(spaceMap)
    expandRows = getExpandRows(spaceMap)
    expandMultiplier = 1000000

    galaxyCount = len(galaxyCoords)
    totalDist = 0
    for i in range(galaxyCount - 1):
        remainingGalaxies = galaxyCoords[i + 1:]
        startCoord = galaxyCoords[i]
        for endCoord in remainingGalaxies:
            totalDist = totalDist + abs(startCoord[0] - endCoord[0])
            totalDist = totalDist + abs(startCoord[1] - endCoord[1])

            xExpandCount = getExpandCrossCount(startCoord[0], endCoord[0], expandCols)
            totalDist = totalDist + ((xExpandCount * expandMultiplier) - xExpandCount)
            yExpandCount = getExpandCrossCount(startCoord[1], endCoord[1], expandRows)
            totalDist = totalDist + ((yExpandCount * expandMultiplier) - yExpandCount)

    print(totalDist)

part2(input)
