import re, logging, os, math
inputs = __import__("inputs")

INPUT = inputs.get_bus_data(2020, 14)
EXAMPLE = inputs.get_bus_data(2020, 14, True)

# %%



# %%

EX_RESULT_P1 = part_one(EXAMPLE)
assert EX_RESULT_P1 == 295
print("Part one: {}".format(part_one(INPUT)))

EX_RESULT_P2 = part_two(EXAMPLE)
assert EX_RESULT_P2 == 1068781
print("Part two: {}".format(part_two(INPUT)))
