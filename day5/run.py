#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

def get_seat_id2(boarding_pass):
  b = ''

  for c in boarding_pass:
    b += '1' if c in 'BR' else '0'

  return int(b, 2)

def part1():
  pi = parse_input()

  return max(map(get_seat_id2, pi))

def part2():
  pi = parse_input()

  seat_ids = set(map(get_seat_id2, pi))

  for seat_id in seat_ids:
    if (seat_id + 1) not in seat_ids:
      return seat_id + 1

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
