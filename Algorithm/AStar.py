import utils

class AStar:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def writePathInFile(self):
        print(utils.is_goal(self.puzzle))
