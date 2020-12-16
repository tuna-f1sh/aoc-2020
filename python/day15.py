import re, logging, os, math, re
inputs = __import__("inputs")

INPUT = [int(x) for x in inputs.get_input(2020, 15)[0].split(',')]
EXAMPLE = inputs.get_input(2020, 15, True)
EXAMPLE = [x.split(',') for x in EXAMPLE]

# %%

def part_one(numbers: list, end=2020):
    spoken = dict()
    speak = 0

    for i in range(end):
        if i < len(numbers):
            number = numbers[i]
        else:
            number = speak

        if number in spoken:
            # spoken once say 0
            if spoken[number][1] == 0:
                speak = 0
            # otherwise it's difference between most recent and oldest
            else:
                speak = spoken[number][1] - spoken[number][0]
        else:
            speak = number

        # print(speak)
        if speak in spoken:
            # second time, keep track of recent
            if spoken[speak][1] == 0:
                spoken[speak][1] = i + 1
            # already spoken twice, push most recent in
            else:
                spoken[speak][0] = spoken[speak][1]
                spoken[speak][1] = i + 1
        else:
            spoken[speak] = [i + 1, 0]
        # print(spoken)

    return speak

# %%

EX_RESULT_P1 = part_one([int(i) for i in EXAMPLE[0]])
assert EX_RESULT_P1 == 436
EX_RESULT_P1 = part_one([int(i) for i in EXAMPLE[1]])
assert EX_RESULT_P1 == 1
EX_RESULT_P1 = part_one([int(i) for i in EXAMPLE[2]])
assert EX_RESULT_P1 == 10
EX_RESULT_P1 = part_one([int(i) for i in EXAMPLE[3]])
assert EX_RESULT_P1 == 27
print("Part one: {}".format(part_one(INPUT, 2020)))
print("Part two: {}".format(part_one(INPUT, 30000000)))
