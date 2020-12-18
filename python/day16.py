import re, logging, os, math, re
from functools import reduce
inputs = __import__("inputs")

INPUT = inputs.get_input(2020, 16)
EXAMPLE = inputs.get_input(2020, 16, True)
INPUT_RAW = inputs.get_input(2020, 16, raw=True)
EXAMPLE_RAW = inputs.get_input(2020, 16, True, raw=True)

RANGE_RE = re.compile(r"\s([0-9]+)\-([0-9]+)+")
FIELD_RE = re.compile(r"^([a-z]+|[a-z]+\s[a-z]+):.+$")

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

def get_ranges(tickets: list):
    ranges = set()

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
    return ranges

def get_fields(tickets: list):
    fields = dict()

    # fill ranges
    for line in tickets:
        # still reading valid fields
        values = RANGE_RE.findall(line)
        field = FIELD_RE.findall(line)
        if len(values) == 2 and len(field) == 1:
            ranges = [(int(values[0][0]), int(values[0][1]) + 1), (int(values[1][0]), int(values[1][1]) + 1)]
            fields[field[0]] = ranges
        else:
            break
    return fields

def get_start(tickets: list):
    # find where tickets to check start
    for i, t in enumerate(tickets):
        if t == "nearby tickets:":
            return i+1

    return None

def part_one(tickets: list):
    # repeated invalid allowed so not a set..
    # invalid = set()
    invalid = []
    
    ranges = get_ranges(tickets)
    nearby_start = get_start(tickets)

    # look at nearby values and check if valid by seeing if inside one of the ranges
    for line in tickets[nearby_start:]:
        line_ints = [int(i) for i in line.split(',')]
        for i in line_ints:
            if not value_valid_threshold(i, ranges):
                invalid.append(i)

    return sum(invalid)

def in_field(n, field, fields):
    for r in fields[field]:
        if n in range(r[0], r[1]):
            return True
    return False

def part_two(raw_tickets: list):
    parts = [x.strip().split('\n') for x in raw_tickets.split('\n\n')]

    fields = get_fields(parts[0])
    ranges = get_ranges(parts[0])
    my_ticket = [int(x) for x in parts[1][1].split(',')]
    tickets = parts[2][1:]
    valid = []

    for line in tickets:
        line_ints = [int(i) for i in line.split(',')]
        invalid = False
        for i in line_ints:
            if not value_valid_threshold(i, ranges):
                invalid = True
                break
        if not invalid:
            valid.append(line_ints)

    not_possible = [set() for x in range(len(my_ticket))]

    # run through valid tickets
    for tick in valid:
        # run through each number
        for i, num in enumerate(tick):
            # check each field
            for field in fields:
                # add index of fields it cannot be
                if not in_field(num, field, fields):
                    not_possible[i].add(field)

    fieldnames = set(fields.keys())
    possible = [fieldnames - i for i in not_possible]

    count = sorted(list((len(v), k) for k, v in enumerate(possible)))
    for i, f1 in enumerate(count[:-1]):
        s1 = possible[f1[1]]
        for _, f2 in count[i + 1:]:
            possible[f2] -= s1 & possible[f2]
    fieldmapping = [f for s in possible for f in s]
    mydepartures = [n for n, f in zip(my_ticket, fieldmapping) if f[:9] == 'departure']

    return reduce(lambda x, y: x*y, mydepartures)

# %%

EX_RESULT_P1 = part_one(EXAMPLE)
assert EX_RESULT_P1 == 71
print("Part one: {}".format(part_one(INPUT)))
print("Part two: {}".format(part_two(INPUT_RAW)))
