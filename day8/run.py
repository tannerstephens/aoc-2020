#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split()

def parse_input():
  return [[puzzle_input[i], int(puzzle_input[i+1])] for i in range(0, len(puzzle_input), 2)]

class VM:
  def __init__(self, insts=[]):
    self.acc = 0
    self.header = 0
    self.insts = insts

  def load_insts(self, insts):
    self.insts = insts

  def run(self):
    l = len(self.insts)

    seen = set()

    while self.header != l:
      inst = self.insts[self.header]

      if self.header in seen:
        return False, self.acc

      seen.add(self.header)

      if inst[0] == 'acc':
        self.acc += inst[1]
      elif inst[0] == 'jmp':
        self.header += inst[1] - 1

      self.header += 1

    return True, self.acc


def part1():
  pi = parse_input()

  return VM(pi).run()[1]

def part2():
  pi = parse_input()

  replace = {'nop': 'jmp', 'jmp': 'nop'}

  for i in range(len(pi)):
    inst = pi[i]

    if inst[0] in replace:
      pi[i][0] = replace[inst[0]]

      status, res = VM(pi).run()

      if(status):
        return res

      pi[i][0] = replace[inst[0]]


def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
