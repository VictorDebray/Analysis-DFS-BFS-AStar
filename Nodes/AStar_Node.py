import movements
from Nodes.BestFS_Node import BestFSNode as Parent


class AStarNode(Parent):

    def __init__(self, move_name, prev_dir, puzzle, o_index, w, h, heuristic_func):
        super().__init__(move_name, prev_dir, puzzle, o_index, w, h, heuristic_func)
        self.h_cost = self.heuristic(puzzle, w, h)
        self.g_cost = 0.0
        self.f_cost = self.h_cost

