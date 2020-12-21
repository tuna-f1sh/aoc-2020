import re, logging, os, math, re
from collections import defaultdict
inputs = __import__("inputs")

INPUT = inputs.get_input(2020, 18)
EXAMPLE = inputs.get_input(2020, 18, True)

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

    for char in line:
        if char == ' ':
            continue
        if char.isdigit():
            if first:
                value = int(char)
                first = False
            else:
                value = value * int(char) if operator == '*' else value + int(char)
        else:
            operator = char

    return value

def precedence(op: str, part=1) -> int:
    """
    Returns precedence of operator or 0

    >>> precedence('+', part=1)
    1
    >>> precedence('+', part=2)
    2
    >>> precedence('*', part=2)
    1
    >>> precedence('x')
    0

    """
    if op == '+':
        return 1 if part == 1 else 2
    elif op == '*':
        return 1
    return 0

def operate(term1: int, term2: int, op: str) -> int:
    """
    Return char op on term1 and term2

    >>> operate(5, 4, '+')
    9
    >>> operate(5, 4, '*')
    20

    :param term1 int
    :param term2 int: 
    :param op str: '+' or '*'
    :rtype int: calculated value
    """
    if op == '+':
        return term1 + term2
    elif op == '*':
        return term1 * term2
    else:
        raise ValueError


def calculate(line: str, part=1) -> int:
    """
    Calculates a line using left to right as precedence, including parenthesis

    >>> calculate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")
    13632
    >>> calculate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", part=2)
    23340

    :param line str: line of single digits, +/* operators or parenthesis ()
    :param part int: part 1 or 2 calculation
    :rtype int
    """
    terms, ops = [], []

    def combine_terms():
        term1, term2 = terms.pop(), terms.pop()
        op = ops.pop()
        terms.append(operate(term1, term2, op))

    def combine_terms_eval():
        term1, term2 = terms.pop(), terms.pop()
        op = ops.pop()
        terms.append(eval(f"{term1} {op} {term2}"))

    for c in line:
        if c == ' ':
            continue
        if c.isdigit():
            terms.append(int(c))
        elif c == '(':
            ops.append(c)
        elif c == ')':
            # work backwards calculating inside brackets
            while len(ops) and ops[-1] != '(':
                combine_terms()
            ops.pop()
        elif c == '*' or c == '+':
            while len(ops) and precedence(ops[-1], part) >= precedence(c, part):
                combine_terms()
            ops.append(c)

    while len(ops):
        combine_terms()

    return terms[-1]

def part_one(equations: list) -> int:
    result = 0
 
    for line in equations:
        result += calculate(line)

    return result

def part_two(equations: list) -> int:
    result = 0
 
    for line in equations:
        result += calculate(line, 2)

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
