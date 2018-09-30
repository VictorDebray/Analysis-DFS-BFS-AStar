def is_goal(puzzle):
    arr = [x[0] for x in puzzle]
    if arr is sorted(arr):
        return True
    return False


def clean(node, open_states, closed_states):
    for i, item in enumerate(node.nodes):
        for it in open_states:
            if it.state == item.state:
                del node.nodes[i]
        for it in closed_states:
            if it.state == item.state:
                del node.nodes[i]
