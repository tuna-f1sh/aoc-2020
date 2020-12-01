import os

def get_input(year: int, day: int):
    data = open(os.path.join('../input', str(year), 'day{}.txt'.format(day)), 'r').read().strip().split('\n')
    return data

def get_ints(year, day):
    data = get_input(year, day)
    return [int(x) for x in data]
