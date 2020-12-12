#!/usr/bin/env python3

from os.path import dirname, realpath
dir_path = dirname(realpath(__file__))

with open(f'{dir_path}/input') as f:
  puzzle_input = f.read().split()

def parse_input():
  out = [['.'] + list(line) + ['.'] for line in puzzle_input]
  out = [['.' for _ in range(len(out[0]))]] + out + [['.' for _ in range(len(out[0]))]]

  return out

def print_board(board):
  for line in board:
    print(''.join(line))

def count_alive(board, x, y, memo, extend):
  if y not in memo:
    memo[y] = {}

  if x not in memo[y]:
    memo[y][x] = []

    for dy in range(-1,2):
      for dx in range(-1,2):
        if dx == 0 and dy == 0:
          continue
        ly = y+dy
        lx = x+dx

        try:
          if extend:
            while (0 <= lx) and (0 <= ly) and (board[ly][lx] == '.'):
              lx += dx
              ly += dy


          if board[ly][lx] != '.':
            memo[y][x].append((ly, lx))

        except IndexError:
          pass

  count = 0

  for ly, lx in memo[y][x]:
    count += board[ly][lx] == '#'

  return count

def simulate(board, die=4, extend=False):
  memo = {}

  next_board = [line[:] for line in board]

  change = True

  while change:
    change = False

    for y in range(1, len(board)-1):
      for x in range(1, len(board[0])-1):
        if board[y][x] == '.':
          continue

        count = count_alive(board, x, y, memo, extend)
        if count == 0:
          next_board[y][x] = '#'
        elif count >= die:
          next_board[y][x] = 'L'
        else:
          next_board[y][x] = board[y][x]

        change = change or (board[y][x] != next_board[y][x])

    board, next_board = (next_board, board)

  s = 0
  for line in board:
    s += line.count('#')

  return s


def part1():
  board = parse_input()

  return simulate(board)

def part2():
  pi = parse_input()

  return simulate(pi, die=5, extend=True)

def main():
  part1_res = part1()
  print(f'Part 1: {part1_res}')

  part2_res = part2()
  print(f'Part 2: {part2_res}')

if __name__ == '__main__':
  main()
