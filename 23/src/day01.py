from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2023, day=1))

def convertNums(string):
    if string == '': return string
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    compoundDigits = ['oneight', 'twone', 'threeight', 'fiveight', 'sevenine', 'eightwo', 'eighthree', 'nineight']
    for entry in digits:
        if string.startswith(entry):
            for compound in compoundDigits:
                if string.startswith(compound):
                    return str(digits.index(entry)) + convertNums(string[len(entry)-1:])
            return str(digits.index(entry)) + convertNums(string[len(entry):])
    return string[0] + convertNums(string[1:])
    

def part1(data):
    total = 0
    for line in data:
        line = line.replace('\n', '')
        first = None
        last = None
        for char in line:
            if char.isdigit():
                if first == None:
                    first = 10 * int(char)
                last = int(char)
        total += first
        total += last
    print(total)

def part2(data):
    processedLines = []
    for line in data:
        # convert spelled digits into numeric digits
        processedLines.append(convertNums(line))
    part1(processedLines)

part2(input)
