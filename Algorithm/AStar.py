from Nodes import AStar_Node
import utils
import heapq


class AStar:
    def __init__(self, heuristic_func, heuristic_name, puzzle, w, h):
        self.root = AStar_Node.AStarNode('0', -1, puzzle, utils.find_empty_tile_index(puzzle), w, h, heuristic_func, 0)
        self.open_states = [(self.root.h_cost, self.root)]
        self.map_open_states = {self.root.id: self.root}
        self.closed_states = []
        self.map_closed_states = {}
        self.puzzle = puzzle
        self.f = open("puzzleAStar-" + heuristic_name + ".txt", "w")
        self.debug_f = open("debug-puzzleAStar-" + heuristic_name + ".txt", "w")

    def launchSearch(self):

        while self.open_states.__len__() is not 0:
            (h_cost, item) = heapq.heappop(self.open_states)

            if (item.id in self.map_open_states):
                del self.map_open_states[item.id]

            self.debug_f.write(utils.format_move(item))

            if utils.is_goal(item.id):
                utils.solution_path(self.f, item)
                break

            item.do_moves()
            self.closed_states.insert(0, item)
            self.map_closed_states[item.id] = item
            for child_node in item.nodes:
                if utils.is_goal(item.id):
                    utils.solution_path(self.f, item)
                    break
                elif child_node.id not in self.map_closed_states:
                    new_f_cost = child_node.g_cost + child_node.h_cost
                    node_in_open = utils.get_same_node_with_higher_f(child_node, new_f_cost, self.map_open_states)
                    if node_in_open:
                        node_in_open.f_cost = new_f_cost
                    if child_node.id is not self.map_open_states:
                        self.map_open_states[child_node.id] = child_node
                        heapq.heappush(self.open_states, (child_node.f_cost, child_node))
