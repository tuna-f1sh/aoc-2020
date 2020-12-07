import re, logging, os, math, functools
inputs = __import__("inputs")

INPUT = inputs.get_input(2020, 7, raw=True)
EXAMPLE = inputs.get_input(2020, 7, True, raw=True)


def parse_raw(raw):
    bags = re.findall(r"([a-z]+ [a-z]+) bags contain (.+)", raw)
    formula = re.compile(r"(\d+) ([a-z]+ [a-z]+) bag")
    return {bag: {inner: int(n) for n, inner in formula.findall(contents)} for bag, contents in bags}

# PARSED = parse_raw(EXAMPLE)
PARSED = parse_raw(INPUT)

def has_shiny(bag):
    # is it top level or another bag inside can carry?
    return "shiny gold" in PARSED[bag] or any(map(has_shiny, PARSED[bag]))

def part_one():
    # scan through all the bags seeing if it can carry recurisvely our shiny bag
    return sum(map(has_shiny, PARSED))

def count(bag):
    # go through bags multiplying the number of bags each bag within can hold
    return 1 + sum(n * count(inner) for inner, n in PARSED[bag].items())

def part_two():
    return count("shiny gold") - 1


print("Part one: {}".format(part_one()))
print("Part two: {}".format(part_two()))
# print("Part one: {}".format(part_one(INPUT)))
