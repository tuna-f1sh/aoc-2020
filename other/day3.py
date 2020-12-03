import math
from input import get_grid

OPEN = '.'
TREE = '#'

INPUT = get_grid(2020, 3)
EXAMPLE = '..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#'

def traverse(grid, slope):
    """
    How many trees do you encouter traversing the grid from top-left, slode right 3, down 1 to the bottom

    :param grid list: x columns and '\n' rows
    :param slope tuple: slope of traversal (x, y)
    """
    gx = len(grid[0])
    gy = len(grid)
    dx, dy = slope
    hit = 0

    for n, line in enumerate(grid[::dy]):
        if line[(dx*n) % len(line)] == TREE:
            hit += 1

    return hit

print('part one example: {}'.format(traverse(EXAMPLE, (3,1))))
print('part one: {}'.format(traverse(INPUT, (3,1))))

PART2_CORDS = [(1,1), (3,1), (5,1), (7,1), (1,2)]
print('part two: {}'.format(math.prod([traverse(INPUT, c) for c in PART2_CORDS])))
