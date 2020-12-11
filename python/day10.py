import re, logging, os
inputs = __import__("inputs")

logger = logging.getLogger('day10')

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

INPUT = inputs.get_ints(2020, 10)
EXAMPLE = inputs.get_ints(2020, 10, True)

def part_one(numbers, outlet=0, input_range=(1,3)):
    """
    Finds the number of number of differences of input_range between adaptor output joltage, starting from outlet joltage and returns multiple of differences
    >>> part_one([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4], 0, (1,3))
    35

    7 1 joltage differences * 5 3 joltage differences

    :param numbers list[int]: joltage outputs of adaptors in bag
    :param outlet int: joltage of outlet
    :param input_range tuple: difference range
    """
    count = [0,0]
    # sort increasing value
    numbers.sort()
    # add outlet at start
    numbers.insert(0, outlet)
    # built-in adaptor is max adaptor + 3
    joltage_limit = numbers[-1] + input_range[1]
    # Because adapters can only connect to a source 1-3 jolts lower than its rating, in order to use every adapter, you'd need to choose them like this
    for i, x in enumerate(numbers):
        if i + 1 < len(numbers):
            if numbers[i+1] == x + input_range[0]:
                count[0] += 1
            elif numbers[i+1] == x + input_range[1]:
                count[1] += 1
        # last one is higher difference
        else:
            count[1] += 1

    return count[0] * count[1]

def count_ways(numbers, cache, max_jolt=3):
    # this will start at last and work it's way backwords filling cache
    last_adaptor = numbers[-1]

    if last_adaptor in cache:
        return cache[last_adaptor]

    ret = 0

    # only one combo with two adaptors
    if len(numbers) <= 2:
        return 1
    # find combos between all adaptors upto 3 indexes below
    if last_adaptor - numbers[-2] <= max_jolt:
        ret += count_ways(numbers[:-1], cache)
    if len(numbers) >=3 and last_adaptor - numbers[-3] <= max_jolt:
        ret += count_ways(numbers[:-2], cache)
    if len(numbers) >=4 and last_adaptor - numbers[-4] <= max_jolt:
        ret += count_ways(numbers[:-3], cache)

    # stick it in
    cache[last_adaptor] = ret

    return ret


# set of adaptors and number of next adaptors which could plug into them
PART_TWO_CACHE = {}

def part_two(numbers, cache, outlet=0):
    """
    What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?

    Recursively checks each adaptor for the total number of compatiable next adaptors.

    >>> part_two([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4], {})
    8

    :param numbers list[int]: joltage outputs of adaptors in bag
    :param cache set: reference to store results during recursive search
    :param outlet int: joltage of outlet
    """
    # sort increasing value
    numbers.sort()
    # add outlet at start
    numbers.insert(0, outlet)

    return count_ways(numbers, cache)


EXAMPLE_P1 = part_one(EXAMPLE.copy())
assert EXAMPLE_P1 == (22 * 10)
print("Part one: {}".format(part_one(INPUT.copy())))
EXAMPLE_P2 = part_two(EXAMPLE.copy(), PART_TWO_CACHE)
assert EXAMPLE_P2 == 19208
PART_TWO_CACHE.clear()
print("Part two: {}".format(part_two(INPUT.copy(), PART_TWO_CACHE)))
