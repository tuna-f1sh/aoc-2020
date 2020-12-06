import re, logging, os, math, functools
inputs = __import__("inputs")

logger = logging.getLogger('day6')

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

INPUT = inputs.get_input(2020, 6, split='\n\n')
EXAMPLE = inputs.get_input(2020, 6, True, split='\n\n')

def part_one(groups: list) -> int:
    ret = 0

    for g in groups:
        answers = g.split('\n')

        chars = []
        for ans in answers:
            chars.extend([char for char in ans])
        unique = len(set(chars))
        print("ans: {}, unique {}".format(answers, unique))
        ret += unique

    return ret

def part_two(groups: list) -> int:
    ret = 0
    for g in groups:
        answers = g.split('\n')

        questions = [set(a) for a in answers]
        ret += len(set.intersection(*questions))

    return ret

print("Part one example: {}".format(part_one(EXAMPLE)))
print("Part one: {}".format(part_one(INPUT)))
print("Part two: {}".format(part_two(INPUT)))
