from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2023, day=4))

testData = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]

def part1(data):
    score = 0

    for line in input:
        line = line.replace('\n', '')
        line = line.replace('  ', ' ')
        numPart = line.split(': ')[1]
        numHalfs = numPart.split(' | ')
        winningNums = numHalfs[0].split(' ')
        myNums = numHalfs[1].split(' ')
        lineScore = 0
        for num in myNums:
            if num in winningNums:
                if lineScore == 0:
                    lineScore = 1
                else:
                    lineScore = 2 * lineScore
        score += lineScore

    print(score)

def part2(data):
    cards = [] # (winning nums, card nums)
    counts = [] # how many of each card I have
    for line in data:
        line = line.replace('\n', '')
        line = line.replace('  ', ' ')
        numPart = line.split(': ')[1]
        numHalfs = numPart.split(' | ')
        winningNums = numHalfs[0].split(' ')
        myNums = numHalfs[1].split(' ')
        cards.append((winningNums, myNums))
        counts.append(1)
    cardCount = 0
    for idx, card in enumerate(cards):
        cardCount += counts[idx]
        matchCount = 0
        for num in card[1]:
            if num in card[0]:
                matchCount += 1
        for i in range(matchCount):
            counts[idx+1+i] += counts[idx]
    print(cardCount)

part2(input)
