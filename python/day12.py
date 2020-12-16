import re, logging, os, math, re
inputs = __import__("inputs")

INPUT = inputs.get_navigation_instructions(2020, 12)
EXAMPLE = inputs.get_navigation_instructions(2020, 12, True)

# %%

def execute_boat_instruction(instruction, degrees, x, y):
    # move forwards in direction
    if instruction[0] == 'F':
        x += instruction[1] * math.cos(math.radians(degrees))
        y += instruction[1] * math.sin(math.radians(degrees))
    # move north
    elif instruction[0] == 'N':
        y += instruction[1]
    # move south
    elif instruction[0] == 'S':
        y -= instruction[1]
    # move east
    elif instruction[0] == 'E':
        x += instruction[1]
    # move west
    elif instruction[0] == 'W':
        x -= instruction[1]
    # move right
    elif instruction[0] == 'R':
        degrees -= instruction[1]
    # move left
    elif instruction[0] == 'L':
        degrees += instruction[1]

    return degrees, x, y

def execute_waypoint_instruction(instruction, waypoint_x, waypoint_y, ship_x, ship_y):
    if instruction[0] == 'F':
        ship_x += waypoint_x * instruction[1]
        ship_y += waypoint_y * instruction[1]
    elif instruction[0] == 'N':
        waypoint_y += instruction[1]
    elif instruction[0] == 'S':
        waypoint_y -= instruction[1]
    elif instruction[0] == 'E':
        waypoint_x += instruction[1]
    elif instruction[0] == 'W':
        waypoint_x -= instruction[1]
    elif instruction[0] == 'R':
        rad = math.radians(-instruction[1])
        rotated_waypoint_x = math.cos(rad) * (waypoint_x) - math.sin(rad) * (waypoint_y)
        rotated_waypoint_y = math.sin(rad) * (waypoint_x) + math.cos(rad) * (waypoint_y)

        waypoint_x = rotated_waypoint_x
        waypoint_y = rotated_waypoint_y
    elif instruction[0] == 'L':
        rad = math.radians(instruction[1])
        rotated_waypoint_x = math.cos(rad) * (waypoint_x) - math.sin(rad) * (waypoint_y)
        rotated_waypoint_y = math.sin(rad) * (waypoint_x) + math.cos(rad) * (waypoint_y)

        waypoint_x = rotated_waypoint_x
        waypoint_y = rotated_waypoint_y

    return waypoint_x, waypoint_y, ship_x, ship_y

def part_one(instructions):
    degrees = 0
    x = 0
    y = 0

    for instruction in instructions:
        degrees, x, y = execute_boat_instruction(instruction, degrees, x, y)
        print("Ship after instruction {}: {} {}".format(instruction, x, y))

    return round(abs(x) + abs(y))

def part_two(instructions):
    waypoint_x = 10
    waypoint_y = 1
    ship_x = 0
    ship_y = 0

    for instruction in instructions:
        waypoint_x, waypoint_y, ship_x, ship_y = execute_waypoint_instruction(instruction, waypoint_x, waypoint_y, ship_x, ship_y)
        print("Ship after instruction: ", ship_x, ship_y)
        print("Waypoint: ", waypoint_x, waypoint_y)

    return round(abs(ship_x) + abs(ship_y))

# %%

assert part_one(EXAMPLE) == 25
part_one(INPUT)
assert part_two(EXAMPLE) == 286
part_two(INPUT)
