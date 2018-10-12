import movements


class Node:

    def __init__(self, move, prev_dir, puzzle, o_index, w, h):
        self.id = ''.join(chr(x + 97) for x in puzzle)
        self.tile_move = move
        self.prev_dir = prev_dir
        self.puzzle = puzzle
        self.width = w
        self.height = h
        self.nodes = []
        self.empty_tile_index = o_index
        self.parent_node = None
        self.depth = 0

    def print_node(self):
        for node in self.nodes:
            print(node.puzzle)
