import utils
import sys
import Node


class DFS:
    def __init__(self, puzzle, w, h):
        self.root = Node.Node('0', -1, puzzle, utils.find_empty_tile_index(puzzle), w, h)
        self.open_states = [self.root]
        self.map_open_states = {self.root.id: self.root}
        self.closed_states = []
        self.map_closed_states = {}
        self.f = open("puzzleDFS.txt", "w")

    def launchSearch(self):
        while self.open_states.__len__() is not 0:
            item = self.open_states.pop(0)
            del self.map_open_states[item.id]
            if utils.is_goal(item.id):
                utils.format_move(self.f, item.tile_move, item.puzzle)
                sys.exit('SUCCESS')
            item.do_moves()
            self.closed_states.insert(0, item)
            self.map_closed_states[item.id] = item
            utils.clean(item, self.map_open_states, self.map_closed_states)
            for it in item.nodes:
                self.open_states.insert(0, it)
                self.map_open_states[it.id] = it
            utils.format_move(self.f, item.tile_move, item.puzzle)

    def writePathInFile(self):
        print('writing from DFS')