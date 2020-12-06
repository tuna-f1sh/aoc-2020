import re, logging, os, math, functools
inputs = __import__("inputs")

logger = logging.getLogger('day5')

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

INPUT = inputs.get_input(2020, 5)
EXAMPLE = inputs.get_input(2020, 5, True)

def part_one(boarding_passes: list) -> int:
    highest = 0
    for p in boarding_passes:
        bpid = get_id(p)
        if bpid > highest:
            highest = bpid

    return highest

def part_two(boarding_passes: list) -> int:
    # get ids sorted incrementing
    ids = [get_id(p) for p in boarding_passes]
    ids.sort()
    # make set unique
    ids_set = set(ids)
    # create set to find missing value
    full_ids = set(range(ids[0], ids[-1] + 1))
    # missing is EOR
    missing = ids_set ^ full_ids

    if len(missing) == 1:
        return list(missing)[0]
    else:
        raise ValueError


def int_bisect_str(bp: str, chars=('F', 'B'), start=[0, 127], num=6) -> int:
    bound = start.copy()
    i = 0

    for char in bp:
        if char not in chars:
            continue
        if char == chars[0]:
            bound[1] = ( bound[0] + bound[1] ) / 2
        elif char  == chars[1]:
            bound[0] = ( bound[0] + bound[1] ) / 2
        logger.debug(bound)
        i += 1

    if i >= num:
        return math.ceil(bound[0])
    else:
        raise ValueError

def get_id(boarding_pass: str) -> int:
    row = int_bisect_str(boarding_pass[:-3])
    column = int_bisect_str(boarding_pass[-3:], chars=('L', 'R'), start=[0, 7], num=3)
    return  row * 8 + column


print("Part one example: {}".format(part_one(EXAMPLE)))
print("Part one: {}".format(part_one(INPUT)))
print("Part two: {}".format(part_two(INPUT)))
