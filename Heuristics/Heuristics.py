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
    for idx, tile in enumerate(puzzle):
        h_cost += math.floor(
            math.sqrt(
                ((idx % w) - goal_positions_array[tile].goal_x) ** 2 +
                ((idx // w) - goal_positions_array[tile].goal_y) ** 2))

    return h_cost


def misplaced(puzzle, w, h):
    h_cost = 0
    goal_array = [1,2,3,4,5,6,7,8,9,10,11,0]
    for idx, tile in enumerate(puzzle):
        if (tile != goal_array[idx]):
            h_cost += 1

    return h_cost
