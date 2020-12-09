import re, logging, os
inputs = __import__("inputs")

logger = logging.getLogger('day9')

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

INPUT = inputs.get_ints(2020, 9)
EXAMPLE = inputs.get_ints(2020, 9, True)

def find_sum(number, numbers):
    """
    Returns True if numbers contains a non-matching pair sum of number

    >>> find_sum(127, [95, 102, 117, 150, 182, 127])
    False
    >>> find_sum(40, [35, 20, 15, 25, 47, 40])
    True

    :param number int: number to find pair sum
    :param numbers list: list of numbers to check
    """
    for num in numbers:
        if num == number:
            continue
        # is the other summing value to make this number in the list?
        logger.debug("Matching sum {} for {} in {}".format(number - num, number, numbers))
        if number - num in numbers:
            return True

    # not found so return false; no sum in list
    logger.debug("No sum for {} in {}".format(number, numbers))
    return False

def part_one(numbers, preamble):
    """
    Finds the first number in numbers which does not have a non-matching pair sum

    :param numbers list: ints to search
    :param preamble int: range in which sum is looked at
    """
    for i, num in enumerate(numbers[preamble:]):
        logger.debug("Test num {}".format(num))
        if not find_sum(num, numbers[i:preamble+i]):
            return num
    return None

def part_two(numbers, target):
    """
    you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

    :param numbers list: ints to check
    :param target int: target value to find contiguous set sum
    """
    acc = 0
    start = 0
    for i, num in enumerate(numbers):
        acc += num

        # rolling move sum removing last start
        while acc > target and start < i-1:
            acc -= numbers[start]
            start += 1

        if acc == target:
            return min(numbers[start:i+1]) + max(numbers[start:i+1])

    return None


print("Part one example: {}".format(part_one(EXAMPLE, 5)))
TARGET = part_one(EXAMPLE, 5)
assert TARGET == 127
print("Part two example: {}".format(part_two(EXAMPLE, TARGET)))
assert part_two(EXAMPLE, TARGET) == 62
TARGET = part_one(INPUT, 25)
print("Part one: {}".format(TARGET))
print("Part two: {}".format(part_two(INPUT, TARGET)))
