from Nodes import AStar_Node
import utils
import heapq
import movements


class AStar:
    def __init__(self, heuristic_func, heuristic_name, puzzle, w, h):
        self.root = AStar_Node.AStarNode('0', -1, puzzle, utils.find_empty_tile_index(puzzle), w, h, heuristic_func)
        self.open_states = [(self.root.f_cost, self.root)]
        self.map_open_states = {self.root.id: self.root}
        self.closed_states = []
        self.map_closed_states = {}
        self.puzzle = puzzle
        self.f = open("puzzleAStar-" + heuristic_name + ".txt", "w")
        self.debug_f = open("debug-puzzleAStar-" + heuristic_name + ".txt", "w")

    def launchSearch(self):
        while len(self.open_states) is not 0:
            (h_cost, item) = heapq.heappop(self.open_states)
            if item.id in self.map_open_states:
                del self.map_open_states[item.id]

            self.debug_f.write(utils.format_move(item))

            if utils.is_goal(item.id):
                utils.solution_path(self.f, item)
                break

            self.closed_states.insert(0, item)
            self.map_closed_states[item.id] = item
            for (idx, it) in enumerate(movements.movements_array):
                if item.prev_dir == it.counter_move:
                    continue
                (new_empty_tile_index, move_name, new_puzzle) = it.func(item.puzzle, item.empty_tile_index,
                                                                        item.width, item.height)
                if new_puzzle is None:
                    continue
                child_node = AStar_Node.AStarNode(move_name, it.move, new_puzzle,
                                                  new_empty_tile_index, item.width,
                                                  item.height, item.heuristic)
                child_node.g_cost = utils.g_cost_movement(idx)

                if child_node.id in self.map_closed_states:
                    continue

                temp_g_cost = child_node.g_cost + item.g_cost
                if child_node.id is not self.map_open_states:
                    self.map_open_states[child_node.id] = child_node
                    heapq.heappush(self.open_states, (child_node.f_cost, child_node))
                elif temp_g_cost >= child_node.g_cost:
                    continue
                child_node.parent_node = item
                child_node.g_cost = temp_g_cost
                child_node.f_cost = temp_g_cost + child_node.h_cost
