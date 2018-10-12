import movements
from Node import Node as Parent


class DFSNode(Parent):

    def __init__(self, move, prev_dir, puzzle, o_index, w, h):
        super().__init__(move, prev_dir, puzzle, o_index, w, h)
        self.depth = 0

    def do_moves(self):
        for it in movements.movements_array:
            if self.prev_dir != it.counter_move:
                (new_empty_tile_index, state, new_puzzle) = it.func(self.puzzle, self.empty_tile_index, self.width,
                                                                    self.height)
                if new_puzzle is not None:
                    node = DFSNode(state, it.move, new_puzzle, new_empty_tile_index, self.width, self.height)
                    node.depth = self.depth + 1
                    node.parent_node = self
                    self.nodes.insert(0, node)
