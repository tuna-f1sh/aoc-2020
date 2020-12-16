import re, logging, os, math, re
inputs = __import__("inputs")

INPUT = inputs.get_input(2020, 14)
EXAMPLE = inputs.get_input(2020, 14, True)

MASK_RE = re.compile(r"^mask\s=\s([A-Z0-9]+)$")
MEM_RE = re.compile(r"^mem\[([0-9]+)\]\s=\s([0-9]+)$")

# %%

def part_one(program: list):
    # The bitmask is always given as a string of 36 bits
    mask = 0 << 36
    ignore = 0 << 36
    ones = 0 << 36
    memory = [0] * int(math.pow(2,16))

    for line in program:
        if MASK_RE.match(line):
            mask = MASK_RE.findall(line)[0]
            clear = int(mask.replace('X', '1'), 2)
            ones = int(mask.replace('X', '0'), 2)
        else:
            addr, value = MEM_RE.findall(line)[0]
            memory[int(addr)] = (int(value) & clear) | ones

    return sum(memory)

def part_two(program: list):
    # The bitmask is always given as a string of 36 bits
    mask = 0 << 36
    ignore = 0 << 36
    ones = 0 << 36
    memory = [0] * int(math.pow(2,16))

    for line in program:
        if MASK_RE.match(line):
            mask = MASK_RE.findall(line)[0]
            clear = int(mask.replace('X', '1'), 2)
            ones = int(mask.replace('X', '0'), 2)
        else:
            addr, value = MEM_RE.findall(line)[0]
            floating = [len(mask) - i - 1 for i, b in enumerate(mask) if b == 'X']
            and_mask = int(math.pow(2, 32))
            for f in floating:
                and_mask &= not (1 << f)
            addr = int(addr) & and_mask

            for n in range(len(floating)):
                addr_mask = ones
                for i, f in enumerate(floating):
                    addr_mask |= ((n >> i) & 1) << f
                memory[addr & addr_mask] = int(value)


    return sum(memory)

# %%

EX_RESULT_P1 = part_one(EXAMPLE[:4])
assert EX_RESULT_P1 == 165
print("Part one: {}".format(part_one(INPUT)))

EX_RESULT_P2 = part_two(EXAMPLE[4:])
assert EX_RESULT_P2 == 208
# print("Part two: {}".format(part_two(INPUT)))
