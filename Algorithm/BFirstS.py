from Nodes import BestFS_Node
import utils
import heapq


class BFirstS:
    def __init__(self, heuristic_func, heuristic_name, puzzle, w, h):
        self.root = BestFS_Node.BestFSNode('0', -1, puzzle, utils.find_empty_tile_index(puzzle), w, h, heuristic_func)
        self.open_states = [(self.root.h_cost, self.root)]  # open list of states used as a priority queue
        self.map_open_states = {self.root.id: self.root}  # map of open states to make check faster
        self.closed_states = []  # closed states list used as a stack
        self.map_closed_states = {}  # map of closed states to make check faster
        self.puzzle = puzzle
        self.f = open("puzzleBFirst-" + heuristic_name + ".txt", "w")  # debug file output (search path)
        self.debug_f = open("debug-puzzleBFirst-" + heuristic_name + ".txt", "w")  # debug file output (search path)

    def launchSearch(self):
        while len(self.open_states) is not 0:  # while open list is not empty
            (h_cost, item) = heapq.heappop(self.open_states)  # pop first element of open list
            del self.map_open_states[item.id]  # delete element form map too

            self.debug_f.write(utils.format_move(item))  # print debug search

            if utils.is_goal(item.id):  # check if solution is found
                utils.solution_path(self.f, item)
                break

            item.do_moves()  # compute children moves
            self.closed_states.insert(0, item)   # insert visited state in closed list to avoid loops
            self.map_closed_states[item.id] = item  # same in map

            utils.clean(item, self.map_open_states, self.map_closed_states)  # clean duplicates in children
            for it in item.nodes:  # add remaining in open list/map
                heapq.heappush(self.open_states, (it.h_cost, it))
                self.map_open_states[it.id] = it
