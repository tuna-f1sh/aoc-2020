import re, logging, os, math, re
from collections import defaultdict
inputs = __import__("inputs")

INPUT = inputs.get_input(2020, 18)
EXAMPLE = inputs.get_input(2020, 18, True)

PARENTHESIS_RE = re.compile(r"(\(.+\))")
OPERATORS_RE = re.compile(r"(\d+)|(\+|\*)")

# %%

def calc_line(line: str, current=0) -> int:
    """
    Calculates string line of values and operators from left to right as precedence

    Relies on the fact that digits are single chars and everything is space separated

    >>> calc_line("1 + 2 * 3 + 4 * 5 + 6")
    71

    :param line str: string to calculate
    :rtype int: caculated value
    """
    value = 0
    operator = '+'
    first = True
    skippy = False

    for char in line:
        if char == ' ':
            continue
        # skip until outside parenthesis
        # if skippy:
        #     if char == ')':
        #         skippy = False
        #     continue
        # # break on parenthesis, which should have been calculated into current
        # if char == '(':
        #     if first:
        #         skippy = True
        #     else:
        #         value = value * current if operator == '*' else value + current
        #     break
        if char.isdigit():
            if first:
                value = int(char)
                first = False
            else:
                value = value * int(char) if operator == '*' else value + int(char)
        else:
            operator = char

    return value

def part_one(equations: list) -> int:
    result = 0
 
    for line in equations:
        paren = PARENTHESIS_RE.findall(line)
        while len(paren) == 1:
            current = calc_line(paren[1:-1])
            paren.append(PARENTHESIS_RE.findall(paren[0][1:-1])[0])


    return result

# %%

EX_RESULT_P1 = part_one(["1 + 2 * 3 + 4 * 5 + 6"])
assert EX_RESULT_P1 == 71
EX_RESULT_P1 = part_one(["5 + (8 * 3 + 9 + 3 * 4 * 3)"])
assert EX_RESULT_P1 == 437
EX_RESULT_P1 = part_one(["2 * 3 + (4 * 5)"])
assert EX_RESULT_P1 == 26
EX_RESULT_P1 = part_one(["((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"])
assert EX_RESULT_P1 == 13632
print("Part one: {}".format(part_one(INPUT)))
print("Part two: {}".format(part_two(INPUT)))
