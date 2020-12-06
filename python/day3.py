import math
from inputs import get_input

"""
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
"""

OPEN = "."
TREE = "#"

INPUT = get_input(2020, 3)
EXAMPLE = get_input(2020, 3, True)


def traverse(grid, slope):
    """
    How many trees do you encouter traversing the grid from top-left, slode right 3, down 1 to the bottom

    :param grid list: x columns and '\n' rows
    :param slope tuple: slope of traversal (x, y)
    """
    dx, dy = slope
    hit = 0

    # ::dy is interval of slice so move down by y
    for n, line in enumerate(grid[::dy]):
        # does the x cord on that line hit a tree?
        if line[(dx * n) % len(line)] == TREE:
            hit += 1

    return hit


print("Part one example: {}".format(traverse(EXAMPLE, (3, 1))))
print("Part one: {}".format(traverse(INPUT, (3, 1))))

PART2_CORDS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print("Part two example: {}".format(math.prod([traverse(EXAMPLE, c) for c in PART2_CORDS])))
print("Part two: {}".format(math.prod([traverse(INPUT, c) for c in PART2_CORDS])))
