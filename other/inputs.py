import os

def get_input(year: int, day: int, example = False, split = '\n'):
    """
    Get the input for the year and day

    :param year int: year to get
    :param day int: day to get
    :param example bool: example file rather than real
    """
    day_str = 'day{}_example.txt' if example else 'day{}.txt'
    data = open(os.path.join('../input', str(year), day_str.format(day)), 'r').read().strip().split(split)
    return data

def get_ints(year, day, example = False):
    """
    Return list of ints from input file

    :param year int: year to get
    :param day int: day to get
    :param example bool: example file rather than real
    """
    data = get_input(year, day, example)
    return [int(x) for x in data]
