import utils
import sys
import Node

class DFS:
    def __init__(self, puzzle, w, h):
        state = '0'
        root = Node.Node(state, puzzle, w, h)
        open_states = [root]
        closed_states = []

        while open_states is not []:
            item = open_states.pop(0)
            if utils.is_goal(item.puzzle):
                print(item.state + ' ' + item.puzzle)
                sys.exit('SUCCESS')
            item.do_moves()
            closed_states.insert(0, item)
            utils.clean(item, open_states, closed_states)
            for it in item.nodes:
                open_states.append(it)
            print(item.state + ' [', end='')
            first = 0
            for idx, val in item.puzzle:
                if first == 0:
                    print(str(idx), end='')
                    first += 1
                else:
                    print(', ' + str(idx), end='')
            print(']')
            print()

    def writePathInFile(self):
        print('writing from DFS')
