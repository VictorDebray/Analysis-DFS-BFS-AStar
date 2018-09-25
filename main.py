import sys
import argparse

parser = argparse.ArgumentParser(description='Solution to 11 tile puzzle with DFS, BFS and A*')
# P puzzle vector
parser.add_argument('integers', metavar='P', type=int, nargs='+', help=' 11 integers for the puzzle')

args = parser.parse_args()
puzzle = args.integers
print(puzzle)

if len(puzzle) < 11:
    sys.exit("Incorrect number of tiles, must be 11");

seen = set()
uniq = []
for x in puzzle:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
    else:
        sys.exit("Duplicate tile in puzzle, must be unique")
