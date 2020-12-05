#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split('\n')[:-1]

def parse_input():
  return puzzle_input[:]

def get_row(boarding_pass):
  l = 0
  r = 127

  for c in boarding_pass[:7]:
    delta = ((r - l)//2)+1
    if c == "F":
      r -= delta
    else:
      l += delta
  return l

def get_seat(boarding_pass):
  l = 0
  r = 7

  for c in boarding_pass[-3:]:
    delta = ((r - l)//2)+1
    if c == "L":
      r -= delta
    else:
      l += delta

  return l

def get_seat_id(boarding_pass):
  return get_row(boarding_pass)*8 + get_seat(boarding_pass)

def part1():
  pi = parse_input()

  return max([get_seat_id(boarding_pass) for boarding_pass in pi])

def part2():
  pi = parse_input()

  seats_ids = sorted([get_seat_id(boarding_pass) for boarding_pass in pi])

  for i, sid in enumerate(seats_ids):
    if (seats_ids[i+1] == sid+2):
      return sid+1





def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
