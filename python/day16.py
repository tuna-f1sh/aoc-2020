import re, logging, os, math, re
inputs = __import__("inputs")

INPUT = inputs.get_input(2020, 16)
EXAMPLE = inputs.get_input(2020, 16, True)

RANGE_RE = re.compile(r"\s([0-9]+)\-([0-9]+)+")

# %%

def value_valid(value, ranges):
    for r in ranges:
        if value in range(*r):
            return True

# this is quicker
def value_valid_threshold(value, ranges):
    for r in ranges:
        if value >= r[0] and value < r[1]:
            return True

def part_one(tickets: list):
    ranges = set()
    # repeated invalid allowed so not a set..
    # invalid = set()
    invalid = []

    # find where tickets to check start
    for i, t in enumerate(tickets):
        if t == "nearby tickets:":
            nearby_start = i+1
            break

    # fill ranges
    for line in tickets:
        # still reading valid fields
        values = RANGE_RE.findall(line)
        if len(values) == 2:
            vset = [(int(values[0][0]), int(values[0][1]) + 1), (int(values[1][0]), int(values[1][1]) + 1)]
            ranges.add(vset[0])
            ranges.add(vset[1])
        else:
            break

    # look at nearby values and check if valid by seeing if inside one of the ranges
    for line in tickets[nearby_start:]:
        line_ints = [int(i) for i in line.split(',')]
        for i in line_ints:
            if not value_valid_threshold(i, ranges):
                invalid.append(i)

    return sum(invalid)

# %%

EX_RESULT_P1 = part_one(EXAMPLE)
assert EX_RESULT_P1 == 71
print("Part one: {}".format(part_one(INPUT)))
