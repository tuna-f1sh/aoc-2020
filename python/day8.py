import re, logging, os, math, functools
inputs = __import__("inputs")

INPUT = inputs.get_program(2020, 8)
EXAMPLE = inputs.get_program(2020, 8, True)

class GameConsole:
    def __init__(self, program, verbose=False, loops=1):
        self.instructions = {
            'nop': None,
            'acc': lambda i: self.accumulator(i),
            'jmp': lambda a: self.move(offset=a)
        }

        self.verbose = verbose
        self.program = program
        self.acc = 0
        self.ip = 0
        self.loops = loops
        self.loop = 0
        self.seen = set()

    def accumulator(self, inc=1):
        if (self.verbose): print("Accumulate {} + {}".format(self.acc, inc))
        self.acc += inc

    def move(self, address=None, offset=1):
        if address is not None:
            addr = address
        else:
            addr = self.ip + offset
        if (self.verbose): print("{} {} -> {}".format("Jump" if abs(self.ip - addr) > 1 else "Move", self.ip, addr))
        self.ip = addr

    def run(self):
        try:
            while True:
                op = self.program[self.ip][0]
                value = self.program[self.ip][1]

                # increment loop if we're back there and stop if hit number of loops
                if self.ip in self.seen:
                    self.loop += 1
                    self.seen.clear()
                    if self.loop == self.loops: break

                # run the instruction the instruction pointer points to
                self.seen.add(self.ip)
                instruction = self.instructions[op]
                if instruction is not None: instruction(value)
                # yield self.ip, self.acc

                if op != "jmp":
                    self.move()
        except IndexError:
            if self.verbose: print('Instruction overflow: {}!'.format(self.ip))
            # yield self.ip, self.acc

        except KeyError:
            if self.verbose: print('Unknown instruction: {}!'.format(self.program[self.ip]))
            # yield self.ip, self.acc

g = GameConsole(EXAMPLE, True)

def part_one(program, verbose=False):
    gc = GameConsole(program, verbose=verbose, loops=1)
    # for _ in gc.run():
    #     print("Computing...")
    gc.run()

    return gc.acc

def part_two(program, verbose=False):
    gc = GameConsole(program, verbose=verbose, loops=1)
    acc = None

    # brute force change program until the console runs without looping
    for i, op in enumerate(program):
        if op == "acc":
            continue
        # replace jmp with nop and nop with jmp
        new_op = "jmp" if op == "nop" else "nop"
        # splice in the replaced operation, keeping int value
        new_prog = program[:i] + [(new_op, program[i][1])] + program[i+1:]
        # run it
        gc = GameConsole(new_prog, verbose=verbose, loops=1)
        gc.run()
        new_prog.clear()
        # did it run and exit?
        if gc.loop == 0:
            acc = gc.acc
            break

    return acc


print("Part one example: {}".format(part_one(EXAMPLE, verbose=True)))
print("Part one: {}".format(part_one(INPUT, verbose=False)))
print("Part two example: {}".format(part_two(EXAMPLE)))
print("Part two: {}".format(part_two(INPUT)))
