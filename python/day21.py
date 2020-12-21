import re, logging, os, math, re
from collections import defaultdict
inputs = __import__("inputs")

INPUT = inputs.get_input(2020, 21)
EXAMPLE = inputs.get_input(2020, 21, example=True)

ALERGENS_RE = re.compile(r"\(contains\s(\w+)+.*\)$")

# %%

def parse_items(raw: list) -> tuple:
    alergens_ingredients = {}
    ingredients = []

    for line in raw:
        line_ingredients, alergens = line.split("(")
        line_ingredients = set(line_ingredients.strip().split())
        alergens = set(alergens[:-1].replace(',', '').split()[1:])

        ingredients.extend(line_ingredients)

        for item in alergens:
            if item in alergens_ingredients:
                alergens_ingredients[item] &= line_ingredients
            else:
                alergens_ingredients[item] = line_ingredients.copy()

    return ingredients, alergens_ingredients


def part_one(raw: list) -> int:
    """
    Return items that connot possible contain alergen

    :param raw list: list of foods
    """
    ingredients, alergens_ingredients = parse_items(raw)

    safe = []
    for i in set(ingredients):
        if i not in set.union(*alergens_ingredients.values()):
            safe.append(i)

    return sum(ingredients.count(i) for i in safe)

def part_two(raw: list) -> int:
    """
    Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list.

    :param raw list: list of foods
    """
    ingredients, alergens_ingredients = parse_items(raw)

    placed = set()

    while len(placed) < len(alergens_ingredients):
        for ii in alergens_ingredients.values():
            # breakpoint()
            if len(ii) == 1:
                placed |= ii
        alergens_ingredients = {k:(v if len(v) == 1 else v - placed) for k,v in alergens_ingredients.items()}
    return ",".join(list(v)[0] for k,v in sorted(alergens_ingredients.items()))


EX_RESULT_P1 = part_one(EXAMPLE)
assert EX_RESULT_P1 == 5
print("Part one: {}".format(part_one(INPUT)))
print("Part two: {}".format(part_two(INPUT)))
