import movements
from Nodes.BestFS_Node import BestFSNode as Parent


class AStarNode(Parent):

    def __init__(self, move_name, prev_dir, puzzle, o_index, w, h, heuristic_func, g_cost):
        super().__init__(move_name, prev_dir, puzzle, o_index, w, h, heuristic_func)
        self.h_cost = self.heuristic(puzzle, w, h)
        self.g_cost = g_cost
        self.f_cost = 0.0

    def do_moves(self):
        for (idx, it) in enumerate(movements.movements_array):
            if self.prev_dir != it.counter_move:
                (new_empty_tile_index, move_name, new_puzzle) = it.func(self.puzzle, self.empty_tile_index,
                                                                        self.width, self.height)

                if new_puzzle is not None:
                    node = AStarNode(move_name, it.move, new_puzzle,
                                     new_empty_tile_index, self.width,
                                     self.height, self.heuristic, self.g_cost)
                    if idx % 2 is not 0:
                        node.g_cost += 1.41
                    else:
                        node.g_cost += 1.0
                    node.f_cost = node.g_cost + node.h_cost
                    node.parent_node = self
                    self.nodes.insert(0, node)
