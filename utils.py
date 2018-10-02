def is_goal(puzzle):
    return puzzle == [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j'), (11, 'k'), (0, 'l')]

def clean(node, open_states, closed_states, open_list):
    id_node_tup = [(x.id, x) for x in node.nodes]
    for item in id_node_tup:
        if item[0] in open_states:
            node.nodes.remove(item[1])
            break
        for it in closed_states:
            if it.id == item[0]:
                node.nodes.remove(item[1])

# def clean(node, open_states, closed_states):
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