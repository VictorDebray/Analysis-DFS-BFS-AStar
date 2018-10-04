import collections
import movements
from Heuristics import Heuristics

Movement = collections.namedtuple('MovementsTuple',
                                  ['move', 'counter_move', 'func'])

movements_array = [
    Movement(0, 4, movements.move_up),
    Movement(1, 5, movements.move_up_right),
    Movement(2, 6, movements.move_right),
    Movement(3, 7, movements.move_down_right),
    Movement(4, 0, movements.move_down),
    Movement(5, 1, movements.move_down_left),
    Movement(6, 2, movements.move_left),
    Movement(7, 3, movements.move_up_left)
]


class Node:

    def __init__(self, move, prev_dir, puzzle, o_index, w, h):
        self.id = ''.join(chr(x + 97) for x in puzzle)
        self.tile_move = move
        self.prev_dir = prev_dir
        self.puzzle = puzzle
        self.h_cost = Heuristics.manhattan_distance(puzzle)
        self.width = w
        self.height = h
        self.nodes = []
        self.empty_tile_index = o_index

    def do_moves(self):
        for it in movements_array:
            if self.prev_dir != it.counter_move:
                (new_empty_tile_index, state, new_puzzle) = it.func(self.puzzle, self.empty_tile_index, self.width,
                                                                    self.height)
                if new_puzzle is not None:
                    node = Node(state, it.move, new_puzzle, new_empty_tile_index, self.width, self.height)
                    self.nodes.insert(0, node)

    def print_node(self):
        for node in self.nodes:
            print(node.puzzle)

    def __lt__(self, other):
        return self.h_cost <= other.h_cost
