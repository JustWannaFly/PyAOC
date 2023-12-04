from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2023, day=2))

def parseDrawData(drawinput):
    drawinput = drawinput.replace(';', ',')
    data = []
    for draw in drawinput.split(','):
        parts = draw.split(' ')
        data.append((parts[2], int(parts[1])))
    return data

def part1(data):
    sum = 0
    limits = { 'red':12, 'green':13, 'blue':14 }
    for line in data:
        line = line.replace('\n', '')
        limitBreak = False
        parts = line.split(':')
        id = int(parts[0].split(' ')[1])
        drawData = parseDrawData(parts[1])
        for draw in drawData:
            if limits[draw[0]] < draw[1]:
                limitBreak = True
        if not limitBreak:
            sum += id
            limitBreak = False

    print(sum)

def part2(data):
    sum = 0
    for line in data:
        line = line.replace('\n', '')
        parts = line.split(':')
        mins = { 'red':0, 'green':0, 'blue':0 }
        drawData = parseDrawData(parts[1])
        for draw in drawData:
            if mins[draw[0]] < draw[1]:
                mins[draw[0]] = draw[1]
        sum += (mins['red'] * mins['blue'] * mins['green'])

    print(sum)

part2(input)
