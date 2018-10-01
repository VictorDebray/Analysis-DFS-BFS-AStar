def is_goal(puzzle):
    return puzzle == [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'), (9, 'i'), (10, 'j'), (11, 'k'), (0, 'l')]

def clean(node, open_states, closed_states):
    for i, item in enumerate(node.nodes):
        for it in open_states:
            if it.state == item.state:
                del node.nodes[i]
        for it in closed_states:
            if it.state == item.state:
                del node.nodes[i]
