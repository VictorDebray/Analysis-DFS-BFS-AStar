import math

def manhattan_distance(puzzle):
    h_cost = 0
    for idx, tile in enumerate(puzzle):
        if tile == 0:
            vert_moves = (12 - idx - 1) // 4
            horiz_moves = (12 - idx - 1) % 4
        else:
            vert_moves = (tile - idx - 1) // 4
            horiz_moves = (tile - idx - 1) % 4
        hyp = math.floor(math.sqrt(vert_moves ** 2 + horiz_moves ** 2))
        h_cost += hyp
    return h_cost

