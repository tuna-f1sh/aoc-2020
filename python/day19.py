import re, logging, os, math, re
from collections import defaultdict
inputs = __import__("inputs")

INPUT = inputs.get_input(2020, 19, split='\n\n')
EXAMPLE = inputs.get_input(2020, 19, example=True, split='\n\n')

# %%

def parse_rule(rule,rules):
    if rule.isalpha():
        return rule
    elif mo:=re.match(r'^\d+$',rule):
        return f"({parse_rule(rules[rule],rules)})"
    elif mo:=re.search(r'^(.*?).[|].(.*?)$',rule):
        return f"({parse_rule(mo.group(1),rules)}|{parse_rule(mo.group(2),rules)})"
    elif mo:=re.findall(r'(\d+)',rule):
        output = "("
        for res in mo:
            output += f"({parse_rule(res,rules)})"
        output += ")"
        return output

def part_one(raw: list):
    rules = {k:v.strip().replace('"','') for k,v in (line.strip().split(":") for line in raw[0].split("\n"))}
    entries = (line.strip() for line in raw[1].split("\n"))

    pattern = f"^{parse_rule(rules['0'],rules)}$"
    matches = 0

    for entry in entries:
        if re.search(pattern,entry):
            matches+=1

    return matches

EX_RESULT_P1 = part_one(EXAMPLE)
assert EX_RESULT_P1 == 2
print("Part one: {}".format(part_one(INPUT)))
