#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return set(map(int, puzzle_input))

def find_2020_mul(s):
  for item in s:
    look = 2020-item

    if look in s:
      return look * item

def find_2020_mul_3(s):
  iterable = list(s)
  for i, n in enumerate(iterable):
    for n2 in iterable[i+1:]:
      look = 2020 - n - n2

      if look in s:
        return n*n2*look

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
