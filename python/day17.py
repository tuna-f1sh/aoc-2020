import re, logging, os, math, re
from itertools import product
from collections import defaultdict
inputs = __import__("inputs")

INPUT = inputs.get_input(2020, 17)
EXAMPLE = inputs.get_input(2020, 17, True)

DEAD = '.'
ALIVE = '#'
NEIGHBOURS = range(-1, 2)

# %%

def neighborhood(*position):
    """
    Returns cordinates of every neighbor in each diamension

    """
    for diff in product([-1, 0, 1], repeat=len(position)):
        neighbor = tuple(pos + diff[i] for i, pos in enumerate(position))
        yield neighbor

def init_cube_map(start, diamension):
    space = defaultdict(lambda: ".")
    # pad extra diamension since we are given 2d
    padding = (0,) * (diamension - 2)

    for x, line in enumerate(start):
        for y, state in enumerate(line):
            cube = (x, y) + padding
            space[cube] = state

    return space

def update_cubes(space: list):
    cube_to_active_count = defaultdict(int)

    for cube in space:
        if space[cube] == DEAD:
            continue
        for n in neighborhood(*cube):
            cube_to_active_count[n] += n != cube and space[cube] == ALIVE
    for n, count in cube_to_active_count.items():
        if space[n] == ALIVE:
            if count in [2, 3]:
                space[n] = ALIVE
            else:
                space[n] = DEAD
        elif space[n] == DEAD:
            if count == 3:
                space[n] = ALIVE

def run(start, cycles=6, diamension=3):
    space = init_cube_map(start, diamension)

    for _ in range(cycles):
        update_cubes(space)

    return sum(state == ALIVE for state in space.values())

# %%

EX_RESULT_P1 = run(EXAMPLE)
assert EX_RESULT_P1 == 112
print("Part one: {}".format(run(INPUT)))
print("Part two: {}".format(run(INPUT, diamension=4)))
