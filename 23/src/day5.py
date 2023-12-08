from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2023, day=5))
testData = [
'seeds: 79 14 55 13',
'',
'seed-to-soil map:',
'50 98 2',
'52 50 48',
'',
'soil-to-fertilizer map:',
'0 15 37',
'37 52 2',
'39 0 15',
'',
'fertilizer-to-water map:',
'49 53 8',
'0 11 42',
'42 0 7',
'57 7 4',
'',
'water-to-light map:',
'88 18 7',
'18 25 70',
'',
'light-to-temperature map:',
'45 77 23',
'81 45 19',
'68 64 13',
'',
'temperature-to-humidity map:',
'0 69 1',
'1 0 69',
'',
'humidity-to-location map:',
'60 56 37',
'56 93 4',
]

def mapLookup(map, value):
    for entry in map:
        destStart = entry[0]
        srcStart = entry[1]
        rangeLength = entry[2]
        if srcStart <= value and value < srcStart + rangeLength:
            offset = value - srcStart
            return destStart + offset
    
    return value

def part1(data):
    seeds = None
    maps = []
    currentMap = None
    for line in data:
        line = line.replace('\n', '')
        if seeds == None:
            seeds = []
            parts = line.split(': ')[1].split(' ')
            for part in parts:
                seeds.append(int(part))
        elif line == '':
            if not currentMap == None:
                maps.append(currentMap)
        elif ':' in line:
            currentMap = []
        else:
            parts = line.split(' ')
            currentMap.append((int(parts[0]), int(parts[1]), int(parts[2])))
    maps.append(currentMap)
    
    smallLoc = None
    for seed in seeds:
        soil = mapLookup(maps[0], seed)
        fertilizer = mapLookup(maps[1], soil)
        water = mapLookup(maps[2], fertilizer)
        light = mapLookup(maps[3], water)
        temp = mapLookup(maps[4], light)
        humidity = mapLookup(maps[5], temp)
        location = mapLookup(maps[6], humidity)
        if smallLoc == None or smallLoc > location:
            smallLoc = location
    print(smallLoc)

def part2(data):
    seeds = None
    maps = []
    currentMap = None
    for line in data:
        line = line.replace('\n', '')
        if seeds == None:
            seeds = []
            parts = line.split(': ')[1].split(' ')
            temp = None
            for part in parts:
                if temp == None:
                    temp = part
                else:
                    seeds.append((int(temp), int(part)))
                    temp = None
        elif line == '':
            if not currentMap == None:
                maps.append(currentMap)
        elif ':' in line:
            currentMap = []
        else:
            parts = line.split(' ')
            currentMap.append((int(parts[0]), int(parts[1]), int(parts[2])))
    maps.append(currentMap)
    
    smallLoc = None
    for seed in seeds:
        first = seed[0]
        last = first + seed[1]

        for current in range(first, last + 1):
            soil = mapLookup(maps[0], current)
            fertilizer = mapLookup(maps[1], soil)
            water = mapLookup(maps[2], fertilizer)
            light = mapLookup(maps[3], water)
            temp = mapLookup(maps[4], light)
            humidity = mapLookup(maps[5], temp)
            location = mapLookup(maps[6], humidity)
            if smallLoc == None or smallLoc > location:
                smallLoc = location
    print(smallLoc)

part2(input)
