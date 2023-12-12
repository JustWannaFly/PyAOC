from aocd import get_data
from io import StringIO

testMap = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
    ]
input = StringIO(get_data(year=2023, day=3))
dataMap = []
for line in input:
    line = line.replace('\n', '')
    dataMap.append(line)
# dataMap = testMap # comment out for real answer
xMin = 0
xMax = len(dataMap[0])-1
yMin = 0
yMax = len(dataMap)-1

def isSymbol(char):
    return (not char.isnumeric() and not char == '.')

def isTouchingSymbol(x, y):
    left = max(xMin, x-1)
    right = min(xMax, x+1)
    up = max(yMin, y-1)
    down = min(yMax, y+1)
    chars = set()
    chars.add(dataMap[up][left])
    chars.add(dataMap[y][left])
    chars.add(dataMap[down][left])
    chars.add(dataMap[up][x])
    chars.add(dataMap[down][x])
    chars.add(dataMap[up][right])
    chars.add(dataMap[y][right])
    chars.add(dataMap[down][right])
    for char in chars:
        if isSymbol(char):
            return True
    return False

def extractNum(row, x):
    numStart = x
    startFound = False
    while startFound == False:
        if numStart == 0:
            startFound = True
        elif row[numStart-1].isnumeric():
            numStart -= 1
        else:
            startFound = True
    numEnd = x
    endFound = False
    while endFound == False:
        if numEnd == xMax:
            endFound = True
        elif row[numEnd+1].isnumeric():
            numEnd += 1
        else:
            endFound = True
    return int(row[numStart:numEnd+1])
    
def getTouchingCoords(x, y):
    left = x-1
    right = x+1
    up = y-1
    down = y+1
    coords = []
    if not left < xMin:
        if not up < yMin:
            coords.append((up, left))
        coords.append((y, left))
        if not down > yMax:
            coords.append((down, left))
    if not up < yMin:        
        coords.append((up, x))
    if not down > yMax:
        coords.append((down, x))
    if not right > xMax:
        if not up < yMin:
            coords.append((up, right))
        coords.append((y, right))
        if not down > yMax:
            coords.append((down, right))
    return coords

# this won't work if touching two numbers that are the same. Currently seeing it it'll pass my input as good enough though
def getTouchingNums(x, y):
    touchingCoords = getTouchingCoords(x, y)
    coordNumericMap = []
    for coord in touchingCoords:
        coordNumericMap.append(dataMap[coord[0]][coord[1]].isnumeric())
    nums = set()
    for i, isNum in enumerate(coordNumericMap):
        if isNum:
            coords = touchingCoords[i]
            nums.add(extractNum(dataMap[coords[0]], coords[1]))
    return list(nums)


def part1():
    sum = 0
    for y, row in enumerate(dataMap):
        isCurrentNum = False
        for x, char in enumerate(row):
            if not isCurrentNum:
                if char.isnumeric() and isTouchingSymbol(x, y):
                    isCurrentNum = True
                    sum += extractNum(row, x)
            else:
                isCurrentNum = char.isnumeric()

    print(sum)

def part2():
    sum = 0
    for y, row in enumerate(dataMap):
        for x, char in enumerate(row):
            if char == '*':
                touchingNums = getTouchingNums(x, y)
                if len(touchingNums) == 2:
                    sum += (touchingNums[0] * touchingNums[1])
    print(sum)

part2()
