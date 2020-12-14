import re, logging, os, math
inputs = __import__("inputs")

logger = logging.getLogger('day13')

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

INPUT = inputs.get_bus_data(2020, 13)
EXAMPLE = inputs.get_bus_data(2020, 13, True)
INPUT_P2 = inputs.get_bus_data(2020, 13, strs=True)
EXAMPLE_P2 = inputs.get_bus_data(2020, 13, True, strs=True)

# %%

def find_bus(time, buses):
    bus_id = None
    minutes_wait = 0

    # best time is bus interval - lowest remainder
    for i in buses:
        wait = i - (time % i)
        print(wait)
        if wait < minutes_wait or bus_id is None:
            print(f"{i}: {wait} < {minutes_wait}")
            minutes_wait = wait
            bus_id = i

    return  bus_id * minutes_wait

def part_one(bus_info):
    start = bus_info[0]
    buses = bus_info[1]
    return find_bus(start, buses)

def part_two_brute(bus_info):
    start = bus_info[0]
    buses = bus_info[1]
    sequence = [i for i, x in enumerate(buses) if x.isdigit()]
    ids = [int(x) for x in buses if x.isdigit()]

    target = 0

    # search from 0 in steps of first bus since that one is first in sequence
    for x in range(0, int(math.pow(2,64)), ids[0]):
        gaps = [b - (x % b) if x % b else 0 for b in ids]
        if gaps == sequence:
            print(f"Found sequence time: {x} ({gaps},{sequence})")
            target = x
            break

    return target


def get_modular_equations(buses):
    k = 0

    sequence = [i for i, x in enumerate(buses) if x.isdigit()]
    ids = [int(x) for x in buses if x.isdigit()]
    modular_equations = [(-k % ids[i], ids[i]) for i, k in enumerate(sequence)]

    return modular_equations

def solve_crt(modular_equations: list):
    remainder_pair = (0, 1) # remainder, coefficient

    for me in modular_equations:
        coefficient = remainder_pair[1]

        for k in range(1, me[1]):
            if (coefficient * k) % me[1] == 1:
                remainder_pair = ((((me[0] - remainder_pair[0]) * k) % me[1]) * remainder_pair[1] + remainder_pair[0], remainder_pair[1] * me[1])
                break

    return remainder_pair

def part_two_crt(bus_info):
    buses = bus_info[1]
    modular_equations = get_modular_equations(buses)

    return solve_crt(modular_equations)[0]

# %%

EXAMPLE_P1 = part_one(EXAMPLE)
assert EXAMPLE_P1 == 295
print("Part one: {}".format(part_one(INPUT)))

EX_RESULT_P2 = part_two_brute(EXAMPLE_P2)
assert EX_RESULT_P2 == 1068781
# print("Part two: {}".format(part_two_brute(INPUT_P2)))
EX_RESULT_P2 = part_two_crt(EXAMPLE_P2)
assert EX_RESULT_P2 == 1068781
EXAMPLE_P2_2 = [0, "67,7,x,59,61".split(',')]
EX_RESULT_P2 = part_two_crt(EXAMPLE_P2_2)
assert EX_RESULT_P2 == 1261476
EXAMPLE_P2_2 = [0, "1789,37,47,1889".split(',')]
EX_RESULT_P2 = part_two_crt(EXAMPLE_P2_2)
assert EX_RESULT_P2 == 1202161486
print("Part two: {}".format(part_two_crt(INPUT_P2)))
