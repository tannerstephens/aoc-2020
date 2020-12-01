#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return list(map(int, puzzle_input))

def find_2020_mul(l):
  for i, n in enumerate(l):
    for n2 in l[i+1:]:
      if (n + n2) == 2020:
        return n*n2

def find_2020_mul_3(l):
  for i, n in enumerate(l):
    for n2 in l[i+1:]:
      for n3 in l[i+2:]:
        if (n + n2 + n3) == 2020:
          return n*n2*n3

def part1():
  pi = parse_input()

  return find_2020_mul(pi)

def part2():
  pi = parse_input()

  return find_2020_mul_3(pi)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
