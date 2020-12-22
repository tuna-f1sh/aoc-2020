import re, logging, os, math, re
from collections import defaultdict
inputs = __import__("inputs")

INPUT = inputs.get_input(2020, 22, split='\n\n')
EXAMPLE = inputs.get_input(2020, 22, example=True, split='\n\n')

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
    player_cards = ([int(x) for x in raw[0].split()[2:]], [int(x) for x in raw[1].split()[2:]])
    r = 1

    # play until one player has all cards
    while len(player_cards[0]) > 0 and len(player_cards[1]) > 0:
        c0, c1 = [player_cards[0].pop(0), player_cards[1].pop(0)]
        if c0 > c1:
            player_cards[0].extend([c0, c1])
            print(f"round {r} player 1 wins: {c0} > {c1}: {player_cards}")
        elif c1 > c0:
            player_cards[1].extend([c1, c0])
            print(f"round {r} player 2 wins: {c1} > {c0}: {player_cards}")
        r += 1

    winner = player_cards[1] if len(player_cards[0]) == 0 else player_cards[0]
    ret = 0

    ret = sum(map(lambda x, i: x * i, winner, range(len(winner), 0, -1)))

    return ret


def part_two(raw: list) -> int:
    return 0

# %%

EX_RESULT_P1 = part_one(EXAMPLE)
assert EX_RESULT_P1 == 306
print("Part one: {}".format(part_one(INPUT)))
# print("Part two: {}".format(part_two(INPUT)))
