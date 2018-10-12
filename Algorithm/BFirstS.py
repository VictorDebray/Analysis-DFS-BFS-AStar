import BFirst_Node
import sys
import utils
import heapq


class BFirstS:
    def __init__(self, puzzle, w, h, depth_max):
        self.root = BFirst_Node.BestFSNode('0', -1, puzzle, utils.find_empty_tile_index(puzzle), w, h)
        self.open_states = [(self.root.h_cost, self.root)]
        self.map_open_states = {self.root.id: self.root}
        self.closed_states = []
        self.map_closed_states = {}
        self.puzzle = puzzle
        self.depth_max = depth_max
        self.f = open("puzzleBFirst-h1.txt", "w")
        self.debug_f = open("debug-puzzleBFirst-h1.txt", "w")

    def launchSearch(self):

        while self.open_states.__len__() is not 0:
            (h_cost, item) = heapq.heappop(self.open_states)
            del self.map_open_states[item.id]
            self.debug_f.write(utils.format_move(item))
            if utils.is_goal(item.id):
                utils.solution_path(self.f, item)
                break
            item.do_moves()
            self.closed_states.insert(0, item)
            self.map_closed_states[item.id] = item
            utils.clean(item, self.map_open_states, self.map_closed_states)
            for it in item.nodes:
                heapq.heappush(self.open_states, (it.h_cost, it))
                self.map_open_states[it.id] = it
