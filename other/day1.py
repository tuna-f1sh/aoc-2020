from inputs import get_ints

INPUT = get_ints(2020, 1)

def find_sum_multiple(values, part = 1):
    found = False
    z = 1

    for i, v in enumerate(values):
        for j, x in enumerate(values):
            if i == j:
                continue
            if part == 2:
                for k, z in enumerate(values):
                    if i == k or j == k:
                        continue
                    if (v + x + z) == 2020:
                        found = True
                        break
            else:
                if (v + x) == 2020:
                    found = True
                    break
            if found:
                break
        if found:
            break

    return v * x * z

print('part one: {}'.format(find_sum_multiple(INPUT, 1)))
print('part two: {}'.format(find_sum_multiple(INPUT, 2)))
