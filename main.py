#!/usr/bin/python

import sys
import argparse

from Algorithm.DFS import DFS
from Algorithm.BFirstS import BFirstS
from Algorithm.AStar import AStar


def preparePuzzle(input, w, h):
    seen = set()
    puzzle = [0 for x in range(w * h)]

    index = 0
    for i, x in enumerate(input):
        if x in seen:
            sys.exit("Duplicate tile in puzzle, must be unique")
        else:
            puzzle[index] = x
        seen.add(x)
        index += 1

    print(puzzle)
    return puzzle


def main():
    parser = argparse.ArgumentParser(description='Solution to 11 tile puzzle with DFS, BFirst and A*')
    # P puzzle vector
    parser.add_argument('integers', metavar='P', type=int, nargs='+', help=' 11 integers for the puzzle')

    args = parser.parse_args()
    input = args.integers

    if len(input) < 11:
        sys.exit("Incorrect number of tiles, must be 11")

    w = 4
    h = 3
    puzzle = preparePuzzle(input, w, h)

    # dfs = DFS(puzzle, w, h)
    # dfs.launchSearch()
    # dfs.writePathInFile()
    # DFS.writePathInFile() With heuristic h2

    bfs = BFirstS(puzzle, w, h)
    bfs.launchSearch()
    bfs.writePathInFile()
    # BFirst.writePathInFile() With heuristic h2

    # aStar = AStar(puzzle)
    # aStar.writePathInFile()
    # AStar.writePathInFile() With heuristic h2


if __name__ == "__main__":
    main()

# node = node.Node(Puzzle, w, h)
# x, y = node.do_move()
# print(x, y)
