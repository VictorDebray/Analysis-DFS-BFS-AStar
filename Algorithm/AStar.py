import utils
import sys
import movements
from Nodes.AStarNode import AStarNode
from Heuristics import Heuristics

class AStar:
    def __init__(self, puzzle, width, height):
        self.width = width
        self.height = height
        self.current_node = None

        root = AStarNode(None, puzzle,
                         utils.find_empty_tile_index(puzzle), '0',
                         0, 0)

        self.open_list = {root.id: root}
        self.closed_list = {}
        self.solutionPath = []

        # Stored for faster computation
        self.empty_tile_index = utils.find_empty_tile_index(root.layout)

    def findLowestFCost(self):
        min_f_cost = sys.maxsize
        selected_node = {}
        for hash, node in self.open_list.items():
            if (node.f_cost < min_f_cost):
                min_f_cost = node.f_cost
                selected_node = node

        self.current_node = selected_node

        self.open_list.pop(self.current_node.id)
        self.closed_list[self.current_node.id] = self.current_node

    def appendNextNodesInOpenList(self):

        # Simulate moves to the next possible positions
        for it in movements.movements_array:
            (new_empty_tile_index, move_name, new_puzzle) \
                = it.func(self.current_node.layout, self.empty_tile_index,
                          self.width, self.height)

            if (new_puzzle is None):
                continue

            # Create new node with computed costs
            new_node = AStarNode(self.current_node, new_puzzle,
                                 new_empty_tile_index, move_name,
                                 self.current_node.g_cost + 1,
                                 Heuristics.manhattan_distance(
                                     new_puzzle, self.width,
                                     self.height))

            if (new_node.id in self.closed_list):
                continue

            # Add the node to the open list for further processing
            # Only if it is not already in the list.
            if (new_node.id not in self.open_list):
                self.open_list[new_node.id] = new_node
            elif (new_node.g_cost < self.open_list[new_node.id].g_cost):
                self.open_list[new_node.id].parent = self.current_node

    def launchSearch(self):
        while True:
            self.findLowestFCost()

            self.appendNextNodesInOpenList()

            if (utils.is_goal(self.current_node.id) is True
               or self.open_list.__len__() is 0):
                break

            print(self.current_node.id,
                  ' ', self.current_node.layout,
                  ' ', self.current_node.h_cost)

        print(self.current_node.layout)
        print(utils.is_goal(self.current_node))
