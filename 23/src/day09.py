from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2023, day=9))
testInput = [
'0 3 6 9 12 15',
'1 3 6 10 15 21',
'10 13 16 21 30 45'
]

def parseInputLists(input):
    rows = []
    for line in input:
        row = []
        parts = line.replace('\n', '').split(' ')
        for part in parts:
            row.append(int(part))
        rows.append(row)
    return rows

def getExtendedList(numList, prepend=False):
    lastNum = None
    diffs = []
    for num in numList:
        if lastNum == None:
            lastNum = num
        else:
            diffs.append(num - lastNum)
            lastNum = num
    allSame = True
    for diff in diffs:
        if not diff == 0:
            allSame = False
    nextNum = None
    if allSame:
        nextNum = numList[-1]
    else:
        diffsWithNext = getExtendedList(diffs, prepend)
        if prepend:
            nextNum = numList[0] - diffsWithNext[0]
        else:
            nextNum = diffsWithNext[-1] + numList[-1]
    if prepend:
        numList.insert(0, nextNum)
    else:
        numList.append(nextNum)
    return numList

def part1(data):
    rows = parseInputLists(data)
    total = 0
    for row in rows:
        nextNum = getExtendedList(row)
        total = total + nextNum[-1]
    print(total)

def part2(data):
    rows = parseInputLists(data)
    total = 0
    for row in rows:
        nextNum = getExtendedList(row, True)
        total = total + nextNum[0]
    print(total)

part2(input)
