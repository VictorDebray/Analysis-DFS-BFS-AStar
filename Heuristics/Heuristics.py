import math
import collections

GoalPosition = collections.namedtuple('PositionsTuple',
                                      ['goal_x', 'goal_y'])

goal_positions_array = [
    GoalPosition(3, 2),
    GoalPosition(0, 0),
    GoalPosition(1, 0),
    GoalPosition(2, 0),
    GoalPosition(3, 0),
    GoalPosition(0, 1),
    GoalPosition(1, 1),
    GoalPosition(2, 1),
    GoalPosition(3, 1),
    GoalPosition(0, 2),
    GoalPosition(1, 2),
    GoalPosition(2, 2)
]


def manhattan_distance(puzzle, w, h):
    h_cost = 0
    manhattan_distance.max_tile_value = w * h - 1
    for idx, tile in enumerate(puzzle):
        current_x = idx % w
        current_y = idx // w
        goal_x = goal_positions_array[tile].goal_x
        goal_y = goal_positions_array[tile].goal_y

        hyp = math.floor(math.sqrt((current_x - goal_x) ** 2 + (current_y - goal_y) ** 2))
        h_cost += hyp

    return h_cost


def diagonal_distance(puzzle, w, h):
    h_cost = 0
    for idx, tile in enumerate(puzzle):
        h_cost += abs(tile - 1 - idx)
    return h_cost
