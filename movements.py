def move_up(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    if y != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[i - w][0], temp[1]
        puzzle[i - w] = temp[0], puzzle[i - w][1]
        return puzzle[i - w][1], puzzle
    return None, None


def move_up_right(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    x = i % w
    if y != 0 and x != w - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[i - w + 1][0], temp[1]
        puzzle[i - w + 1] = temp[0], puzzle[i - w + 1][1]
        return puzzle[i - w + 1][1], puzzle
    return None, None


def move_up_left(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    x = i % w
    if y != 0 and x != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[i - w - 1][0], temp[1]
        puzzle[i - w - 1] = temp[0], puzzle[i - w - 1][1]
        return puzzle[i - w - 1][1], puzzle
    return None, None


def move_down(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    if y != h - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[i + w][0], temp[1]
        puzzle[i + w] = temp[0], puzzle[i + w][1]
        return puzzle[i + w][1], puzzle
    return None, None


def move_down_right(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    x = i % w
    if y != h - 1 and x != w - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[i + w + 1][0], temp[1]
        puzzle[i + w + 1] = temp[0], puzzle[i + 1 + w][1]
        return puzzle[i + w + 1][1], puzzle
    return None, None


def move_down_left(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    x = i % w
    if y != h - 1 and x != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[i + w - 1][0], temp[1]
        puzzle[i + w - 1] = temp[0], puzzle[i + w - 1][1]
        return puzzle[i + w - 1][1], puzzle
    return None, None


def move_right(old_p, i, w, h):
    puzzle = old_p[:]
    x = i % w
    if x != w - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[i + 1][0], temp[1]
        puzzle[i + 1] = temp[0], puzzle[i + 1][1]
        return puzzle[i + 1][1], puzzle
    return None, None


def move_left(old_p, i, w, h):
    puzzle = old_p[:]
    x = i % w
    if x != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[i - 1][0], temp[1]
        puzzle[i - 1] = temp[0], puzzle[i - 1][1]
        return puzzle[i - 1][1], puzzle
    return None, None
