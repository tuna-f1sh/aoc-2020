import re, logging, os
inputs = __import__("inputs")

logger = logging.getLogger('day4')

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

INPUT = inputs.get_input(2020, 4, split='\n\n')
EXAMPLE = inputs.get_input(2020, 4, True, split='\n\n')

REQUIRED = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
EYE_COLOURS = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

VALID_TEST = {
        "byr": lambda x: int(x) >= 1920 and int(x) <= 2020 if is_int(x) else False,
        "iyr": lambda x: int(x) >= 2010 and int(x) <= 2020 if is_int(x) else False,
        "eyr": lambda x: int(x) >= 2020 and int(x) <= 2030 if is_int(x) else False,
        "hgt": lambda x: (int(x[:-2]) >= 150 and int(x[:-2]) <= 193 if x[-2:] == 'cm' else int(x[:-2]) >= 59 and int(x[:-2]) <= 76) if len(x) > 2 else False,
        "hcl": lambda x: x[0] == '#' and x[1:].isdigit(),
        "ecl": lambda x: x in EYE_COLOURS,
        "pid": lambda x: len(x) >= 9 and is_int(x),
        "cid": lambda _: True
}

def is_int(i: int):
    try:
        int(i)
        return True
    except ValueError:
        return False

def part_one(passports):
    count = 0

    for line in passports:
        x = re.findall("([a-z]{3}):", line)
        if REQUIRED.issubset(x):
            count += 1
    
    return count

def part_two(passports):
    count = 0

    for line in passports:
        # https://regex101.com/r/Dn5ubW/1
        x = re.findall("([a-z]{3}):(\\S*)", line)
        present = set()
        [present.add(k[0]) for k in x]
        logging.debug(x)
        logging.debug([VALID_TEST[key](val) for key, val in x])
        if REQUIRED.issubset(present) and all([VALID_TEST[key](val) for key, val in x]):
            count += 1
    
    return count

def is_valid(entry: tuple):
    return VALID_TEST[entry[0]](entry[1])


print("Part one example: {}".format(part_one(EXAMPLE)))
print("Part one: {}".format(part_one(INPUT)))
print("Part two example: {}".format(part_two(EXAMPLE)))
print("Part two: {}".format(part_two(INPUT)))
