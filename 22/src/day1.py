from aocd import get_data
from io import StringIO

input = StringIO(get_data(year=2022, day=1))

def part1():
    big_cal = 0
    current_cal = 0
    for line in input:
        line = line[:-1]
        if (line == ''):
            if (current_cal > big_cal):
                big_cal = current_cal
            current_cal = 0
        else:
            current_cal += int(line)
    print('the biggest number of calories carried is ', big_cal)

def part2():
    big_cals = [0,0,0]
    current_cal = 0
    for line in input:
        line = line[:-1]
        if (line == ''):
            if (current_cal > min(big_cals)):
                big_cals.append(current_cal)
                big_cals.remove(min(big_cals))
            current_cal = 0
        else:
            current_cal += int(line)
    print('The top 3 are carrying ', sum(big_cals))

part2()
