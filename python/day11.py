import re, logging, os
inputs = __import__("inputs")

logger = logging.getLogger('day10')

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

INPUT = inputs.get_input(2020, 11)
EXAMPLE = inputs.get_input(2020, 11, True)

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'
NEIGHBOURS = range(-1, 2)

# %%

def get_seat_state(floor_plan: list, col: int, row: int):
    height = len(floor_plan)
    width = len(floor_plan[0])
    # clamp to boundary
    if col < width and col >= 0 and row < height and row >= 0:
        # return floor_plan[row][col]
        return 1 if floor_plan[row][col] == OCCUPIED else 0
    else:
        # return FLOOR
        return 0

def fill_seats(floor_plan: list):
    height = len(floor_plan)
    width = len(floor_plan[0])
    new = floor_plan.copy()

    for y in range(height):
        row = list(floor_plan[y])
        for x in range(width):
            neighbours = sum(
                get_seat_state(floor_plan, x+xx, y+yy)
                for yy in NEIGHBOURS
                for xx in NEIGHBOURS
            ) - get_seat_state(floor_plan, x, y)

            state = floor_plan[y][x]
            if state != FLOOR:
                # 4 or more adjacent occupied it becomes empty
                if neighbours >= 4 and state == OCCUPIED:
                    row[x] = EMPTY
                # if no neighbours and empty
                elif neighbours == 0 and state == EMPTY:
                    row[x] = OCCUPIED
                # otherwise does not change
        new[y] = "".join(row)

    return new

def part_one(floor_plan: list):
    current = floor_plan
    update = []

    # iterate until chaos stablises
    while True:
        update = fill_seats(current)
        print(current)
        print(update)
        if update == current:
            break
        current = update

    return sum([sum([x == OCCUPIED for x in row]) for row in current])

# %%

EXAMPLE_P1 = part_one(EXAMPLE.copy())
assert EXAMPLE_P1 == 37
print("Part one: {}".format(part_one(INPUT.copy())))
