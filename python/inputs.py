import os

def get_input(year: int, day: int, example = False, split = '\n', raw = False):
    """
    Get the input for the year and day

    :param year int: year to get
    :param day int: day to get
    :param example bool: example file rather than real
    """
    day_str = 'day{}_example.txt' if example else 'day{}.txt'
    if raw:
        data = open(os.path.join('../input', str(year), day_str.format(day)), 'r').read()
    else:
        data = open(os.path.join('../input', str(year), day_str.format(day)), 'r').read().strip().split(split)
    return data

def get_ints(year, day, example=False):
    """
    Return list of ints from input file

    :param year int: year to get
    :param day int: day to get
    :param example bool: example file rather than real
    """
    data = get_input(year, day, example)
    return [int(x) for x in data]

def get_program(year, day, example=False):
    data = get_input(year, day, example)
    return [(x[:3].zfill(3), int(x[3:])) for x in data]

def get_navigation_instructions(year, day, example=False):
    data = get_input(year, day, example)
    return [(line[0], float(line[1:])) for line in data]

def get_bus_data(year, day, example=False, strs=False):
    data = get_input(year, day, example)
    id_strs = data[1].split(',')
    if strs:
        ids = id_strs
    else:
        ids = [int(x) for x in id_strs if x.isdigit()]
    return (int(data[0]), ids)
