import utils
import movements
from Nodes.AStarNode import AStarNode

class AStar:
    def __init__(self, puzzle, width, height):
        self.puzzle = puzzle
        self.width = width
        self.height = height
        self.root = AStarNode(None, puzzle)
        self.open_list = [self.root]
        self.closed_list = []
        self.solutionPath = []

        # Stored for faster computation
        self.empty_tile_index = utils.find_empty_tile_index(self.puzzle)

    def appendMovesInOpenList(self):
        for it in movements.movements_array:
            (new_empty_tile_index, move_name, new_puzzle) \
                = it.func(self.puzzle, self.empty_tile_index,
                          self.width, self.height)

    def launchSearch(self):
        print(utils.is_goal(self.puzzle))

        #while (utils.is_goal(self.puzzle) == False
        #       and self.open_list.__len__() != 0):
        #    self.appendMovesInOpenList()


