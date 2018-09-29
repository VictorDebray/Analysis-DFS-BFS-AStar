import sys
import argparse
import movements

parser = argparse.ArgumentParser(description='Solution to 11 tile puzzle with DFS, BFS and A*')
# P puzzle vector
parser.add_argument('integers', metavar='P', type=int, nargs='+', help=' 11 integers for the puzzle')

args = parser.parse_args()
input = args.integers
print(input)

if len(input) < 11:
    sys.exit("Incorrect number of tiles, must be 11")

seen = set()
w = 4
h = 3
Puzzle = [[0 for x in range(w)] for y in range(h)]

index = 0
for x in input:
    if x in seen:
        sys.exit("Duplicate tile in puzzle, must be unique")
    else:
        Puzzle[index // w][index % w] = x
    index += 1

print(Puzzle)
