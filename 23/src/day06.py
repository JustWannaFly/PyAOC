from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2023, day=6))
testData = [
'Time:      7  15   30',
'Distance:  9  40  200'
]


def calcDistance(holdTime, totalTime):
    movingTime = totalTime - holdTime
    return holdTime * movingTime

def getWinCount(time, record):
    count = 0
    for i in range(time):
        distance = calcDistance(i, time)
        if distance > record:
            count += 1
    return count
        

def part1():
    times = None
    records = None
    for line in input:
        line = line.replace('\n', '')
        if times == None:
            times = []
            parts = line.split(':')[1].split(' ')
            for part in parts:
                if not part == '':
                    times.append(int(part))
        else:
            records = []
            parts = line.split(':')[1].split(' ')
            for part in parts:
                if not part == '':
                    records.append(int(part))
    answer = 1
    for i in range(len(times)):
        winCount = getWinCount(times[i], records[i])
        answer = answer * winCount

    print(answer)

def makeBigNum(numList):
    numString = ''
    for num in numList:
        numString = numString + num
    return int(numString)

def part2():
    time = None
    record = None
    for line in input:
        line = line.replace('\n', '')
        if time == None:
            time = makeBigNum(line.split(':')[1].split(' '))
        else:
            record = makeBigNum(line.split(':')[1].split(' '))
            
    print(getWinCount(time, record))

part2()
