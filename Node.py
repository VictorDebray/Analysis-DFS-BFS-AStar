import movements

def find_empty_tile_index(puzzle):
    index = 0
    for x, val in puzzle:
        if x == 0:
            return index
        index += 1

class Node:
    def __init__(self, puzzle, w, h):
        self.movements_array = [
            movements.move_up,
            movements.move_up_right,
            movements.move_right,
            movements.move_down_right,
            movements.move_down,
            movements.move_down_left,
            movements.move_left,
            movements.move_up_left
]
        self.puzzle = puzzle
        self.width = w
        self.height = h

        self.nodes = []
        self.empty_tile_index = find_empty_tile_index(self.puzzle)

    def do_move(self):
        for fun in self.movements_array:
            new_puzzle = fun(self.puzzle, self.empty_tile_index, self.width, self.height)
            if new_puzzle is not None:
                node = Node(new_puzzle, self.width, self.height)
                self.nodes.append(node)

    def print_node(self):
        for node in self.nodes:
            print(node.puzzle)
