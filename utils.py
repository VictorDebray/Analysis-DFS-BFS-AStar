def is_goal(id):
    return id == 'bcdefghijkla'


def find_empty_tile_index(puzzle):
    index = 0
    for x in puzzle:
        if x == 0:
            return index
        index += 1


def clean(node, map_open_states, map_closed_states):
    id_node_tup = [(x.id, x) for x in node.nodes]
    for item in id_node_tup:
        if item[0] in map_open_states or item[0] in map_closed_states:
            node.nodes.remove(item[1])


def format_move(file, tile_move, puzzle):
    first = 0

    file.write(tile_move + ' [')
    for idx in puzzle:
        if first == 0:
            file.write(str(idx))
            first += 1
        else:
            file.write(', ' + str(idx))
    file.write(']\n')


# def clean(node, open_states, closed_states, open_list):
#     id_node_tup = [(x.id, x) for x in node.nodes]
#     for item in id_node_tup:
#         trig = False
#         for it in open_states:
#             if it.id == item[0]:
#                 trig = True
#                 node.nodes.remove(item[1])
#         for it in closed_states:
#             if it.id == item[0] and trig is False:
#                 node.nodes.remove(item[1])
