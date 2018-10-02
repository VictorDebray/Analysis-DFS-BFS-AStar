import utils
import sys
import Node


def format_move(file, tile_move, puzzle):
    first = 0

    file.write(tile_move + ' [')
    for idx, val in puzzle:
        if first == 0:
            file.write(str(idx))
            first += 1
        else:
            file.write(', ' + str(idx))
    file.write(']\n')


class DFS:
    def __init__(self, puzzle, w, h):
        move = '0'
        root = Node.Node(move, -1, puzzle, utils.find_empty_tile_index(puzzle), w, h)
        open_states = [root]
        map_open_states = {root.id: root}
        closed_states = []
        map_closed_states = {}
        f = open("puzzleDFS.txt", "w")

        while open_states.__len__() is not 0:
            item = open_states.pop(0)
            del map_open_states[item.id]
            if utils.is_goal(item.id):
                format_move(f, item.tile_move, item.puzzle)
                sys.exit('SUCCESS')
            item.do_moves()
            closed_states.insert(0, item)
            map_closed_states[item.id] = item
            utils.clean(item, map_open_states, map_closed_states)
            for it in item.nodes:
                open_states.insert(0, it)
                map_open_states[it.id] = it
            format_move(f, item.tile_move, item.puzzle)

    def writePathInFile(self):
        print('writing from DFS')
