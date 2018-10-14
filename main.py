#!/usr/bin/python

import sys
import argparse

from Heuristics import Heuristics
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
    parser.add_argument('-p', '--puzzle', metavar='tile', type=int, nargs=12, help=' 11 integers for the puzzle')
    parser.add_argument('-d', '--DFSmax', metavar='depth_max', default=5, type=int, help='Depth Max of Depth First Search')
    parser.add_argument('-b', '--BFSmax', metavar='depth_max', default=5, type=int, help='Depth Max of Best First Search')

    args = parser.parse_args()
    input = args.puzzle
    DFS_depth_max = args.DFSmax
    BFS_depth_max = args.BFSmax

    if len(input) < 11:
        sys.exit("Incorrect number of tiles, must be 11")

    w = 4
    h = 3
    puzzle = preparePuzzle(input, w, h)

    dfs = DFS(puzzle, w, h, DFS_depth_max)
    dfs.launchSearch()

    bfs_h1 = BFirstS(Heuristics.diagonal_distance, "h1", puzzle, w, h)
    bfs_h1.launchSearch()
    bfs_h2 = BFirstS(Heuristics.manhattan_distance, "h2", puzzle, w, h)
    bfs_h2.launchSearch()

    aStar = AStar(puzzle, w, h)
    aStar.launchSearch()
    # AStar.writePathInFile() With heuristic h2


if __name__ == "__main__":
    main()

# node = node.Node(Puzzle, w, h)
# x, y = node.do_move()
# print(x, y)
