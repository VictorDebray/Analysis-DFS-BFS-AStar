import math


def manhattan_distance(puzzle, w, h):
    h_cost = 0
    manhattan_distance.max_tile_value = w * h - 1
    for idx, tile in enumerate(puzzle):
        if tile == 0:
            correct_pos_x = manhattan_distance.max_tile_value // w
            correct_pos_y = manhattan_distance.max_tile_value % w
            tile_x = (manhattan_distance.max_tile_value - idx - 1) // w
            tile_y = (manhattan_distance.max_tile_value - idx - 1) % h
        else:
            correct_pos_x = idx // w
            correct_pos_y = idx % h
            tile_x = (tile - 1) // w
            tile_y = (tile - 1) % h
        hyp = math.floor(math.sqrt((tile_x - correct_pos_x) ** 2 + (tile_y - correct_pos_y) ** 2))
        h_cost += hyp
    return h_cost


# def permutation_inversion(puzzle):
#     h_cost = 0
#     for idx, tile in enumerate(puzzle):
#