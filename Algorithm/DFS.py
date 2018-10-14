import utils
from Nodes import DFSNode


class DFS:
    def __init__(self, puzzle, w, h, depth_max):
        self.root = DFSNode.DFSNode('0', -1, puzzle, utils.find_empty_tile_index(puzzle), w, h)
        self.open_states = [self.root]  # open list of states used as a stack
        self.map_open_states = {self.root.id: self.root}  # map of open states to make check faster
        self.closed_states = []  # closed states list used as a stack
        self.map_closed_states = {}  # map of closed states to make check faster
        self.depth_max = depth_max  # depth max of search
        self.debug_f = open("debug-puzzleDFS.txt", "w")  # debug file output (search path)
        self.f = open("puzzleDFS.txt", "w")  # output file (solution path)

    def launchSearch(self):
        while len(self.open_states) is not 0:  # while open list is not empty
            item = self.open_states.pop(0)  # pop first element of open list
            del self.map_open_states[item.id]  # delete element form map too

            self.debug_f.write(utils.format_move(item))  # print debug search

            if utils.is_goal(item.id):  # check if solution is found
                utils.solution_path(self.f, item)
                break
            if item.depth >= self.depth_max + 1:  # check if depth is reached
                continue

            item.do_moves()  # compute children moves
            self.closed_states.insert(0, item)  # insert visited state in closed list to avoid loops
            self.map_closed_states[item.id] = item  # same in map
            utils.clean(item, self.map_open_states, self.map_closed_states)  # clean duplicates in children
            for it in item.nodes:  # add remaining in open list/map
                self.open_states.insert(0, it)
                self.map_open_states[it.id] = it
