from Nodes.Node import Node as Parent
import movements


class BestFSNode(Parent):

    def __init__(self, move_name, prev_dir, puzzle, o_index, w, h, heuristic_func):
        super().__init__(move_name, prev_dir, puzzle, o_index, w, h)
        self.heuristic = heuristic_func
        self.h_cost = self.heuristic(puzzle, w, h)

    def do_moves(self):
        for it in movements.movements_array:
            if self.prev_dir != it.counter_move:
                (new_empty_tile_index, move_name, new_puzzle) = it.func(self.puzzle, self.empty_tile_index,
                                                                        self.width, self.height)

                if new_puzzle is not None:
                    node = BestFSNode(move_name, it.move, new_puzzle,
                                      new_empty_tile_index, self.width,
                                      self.height, self.heuristic)
                    node.parent_node = self
                    self.nodes.insert(0, node)

    def __lt__(self, other):
        return self.h_cost <= other.h_cost
