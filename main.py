#!/usr/bin/python

import sys
import argparse
import random

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


def doDFS(puzzle, w, h, DFS_depth_max):
    dfs = DFS(puzzle, w, h, DFS_depth_max)
    dfs.launchSearch()

def loopOnBFS(puzzles, w, h):
    i = 0
    while (i < puzzles.__len__()):
        print("BFS ", puzzles[i])
        doBFS(puzzles[i], w, h, i)
        i += 1


def doBFS(puzzle, w, h, i):
    # bfs_h1 = BFirstS(Heuristics.misplaced, "h1" + i.__str__(), puzzle, w, h)
    # bfs_h1.launchSearch()

    bfs_h2 = BFirstS(Heuristics.manhattan_distance, "h2" + i.__str__(), puzzle, w, h)
    bfs_h2.launchSearch()



def loopOnAStar(puzzles, w, h):
    for p in puzzles:
        print("AStar", p)
        doAStar(p, w, h)


def doAStar(puzzle, w, h):
    #astar_h1 = AStar(Heuristics.misplaced, "h1", puzzle, w, h)
    #astar_h1.launchSearch()

    astar_h2 = AStar(Heuristics.manhattan_distance, "h2", puzzle, w, h)
    astar_h2.launchSearch()


def main():
    parser = argparse.ArgumentParser(description='Solution to 11 tile puzzle with DFS, BFirst and A*')
    # P puzzle vector
    parser.add_argument('-p', '--puzzle', metavar='tile', type=int, nargs=12, help=' 11 integers for the puzzle')
    parser.add_argument('-d', '--DFSmax', metavar='depth_max', default=5, type=int, help='Depth Max of Depth First Search')

    args = parser.parse_args()
    input = args.puzzle
    DFS_depth_max = args.DFSmax

    if len(input) < 11:
        sys.exit("Incorrect number of tiles, must be 11")

    w = 4
    h = 3
    puzzle = preparePuzzle(input, w, h)

    puzzles = []
    i = 0
    while (i < 10):
        puzzles.append(random.sample(range(0, 12), 12))
        i += 1

    #doDFS(puzzle, w, h, DFS_depth_max)
    loopOnBFS(puzzles, w, h)
    #loopOnAStar(puzzles, w, h)

if __name__ == "__main__":
    main()
