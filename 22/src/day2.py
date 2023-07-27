from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2022, day=2))

def part1(): 
    points = {
        'A': {
            'X': 4, # 1 + 3
            'Y': 8, # 2 + 6
            'Z': 3  # 3 + 0
        },
        'B': {
            'X': 1, # 1 + 0
            'Y': 5, # 2 + 3
            'Z': 9  # 3 + 6
        },
        'C': {
            'X': 7, # 1 + 6
            'Y': 2, # 2 + 0
            'Z': 6  # 3 + 3
        }
    }
    score = 0
    for line in input:
        line = line.replace('\n', '')
        parts = line.split(' ')
        score += points.get(parts[0]).get(parts[1])
    print('predicted score: ', score)

def part2(): 
    points = {
        'A': {
            'X': 3, # 3 + 0
            'Y': 4, # 1 + 3
            'Z': 8  # 2 + 6
        },
        'B': {
            'X': 1, # 1 + 0
            'Y': 5, # 2 + 3
            'Z': 9  # 3 + 6
        },
        'C': {
            'X': 2, # 2 + 0
            'Y': 6, # 3 + 3
            'Z': 7  # 1 + 6
        }
    }
    score = 0
    for line in input:
        line = line.replace('\n', '')
        parts = line.split(' ')
        score += points.get(parts[0]).get(parts[1])
    print('predicted score: ', score)

part2()
