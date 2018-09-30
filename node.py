import movements

movements_array = [
    movements.move_up,
    movements.move_up_right,
    movements.move_right,
    movements.move_down_right,
    movements.move_down,
    movements.move_down_left,
    movements.move_left,
    movements.move_up_left
]


def is_goal(puzzle):
    arr = [x[0] for x in puzzle]
    if arr is sorted(arr):
        return True
    return False


def find_empty_tile_index(puzzle):
    index = 0
    for x, val in puzzle:
        if x == 0:
            return index
        index += 1


class Node:
    def __init__(self, puzzle, w, h):
        self.puzzle = puzzle
        self.width = w
        self.height = h

        self.nodes = []
        self.empty_tile_index = find_empty_tile_index(self.puzzle)

    def do_move(self):
        for fun in movements_array:
            new_puzzle = fun(self.puzzle, self.empty_tile_index, self.width, self.height)
            if new_puzzle is not None:
                node = Node(new_puzzle, self.width, self.height)
                self.nodes.append(node)


        new_puzzle = movements.move_up_right(self.puzzle, self.empty_tile_index, self.width, self.height)
        if new_puzzle is not None:
            self.up_right = Node(new_puzzle, self.width, self.height)

        new_puzzle = movements.move_right(self.puzzle, self.empty_tile_index, self.width)
        if new_puzzle is not None:
            self.right = Node(new_puzzle, self.width, self.height)

        new_puzzle = movements.move_down_right(self.puzzle, self.empty_tile_index, self.width, self.height)
        if new_puzzle is not None:
            self.down_right = Node(new_puzzle, self.width, self.height)

        new_puzzle = movements.move_down(self.puzzle, self.empty_tile_index, self.width, self.height)
        if new_puzzle is not None:
            self.down = Node(new_puzzle, self.width, self.height)

        new_puzzle = movements.move_down_left(self.puzzle, self.empty_tile_index, self.width, self.height)
        if new_puzzle is not None:
            self.down_left = Node(new_puzzle, self.width, self.height)

        new_puzzle = movements.move_left(self.puzzle, self.empty_tile_index, self.width)
        if new_puzzle is not None:
            self.left = Node(new_puzzle, self.width, self.height)

        new_puzzle = movements.move_up_left(self.puzzle, self.empty_tile_index, self.width, self.height)
        if new_puzzle is not None:
            self.up_left = Node(new_puzzle, self.width, self.height)

    def print_node(self):
        print("Up move" + self.up.puzzle)
        print("Up right move" + self.up_right.puzzle)
        print("Right right move" + self.right.puzzle)
        print("Down right move" + self.down_right.puzzle)
        print("Down move" + self.down.puzzle)
        print("Down left move" + self.down_left.puzzle)
        print("Left move" + self.left.puzzle)
        print("Up Left move" + self.up_left.puzzle)
