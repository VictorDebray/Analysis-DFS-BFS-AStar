def move_up(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    new_i = i - w
    if y != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[new_i]
        puzzle[new_i] = temp
        return new_i, chr(new_i + 97), puzzle
    return None, None, None


def move_up_right(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    x = i % w
    new_i = i - w + 1
    if y != 0 and x != w - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[new_i]
        puzzle[new_i] = temp
        return new_i, chr(new_i + 97), puzzle
    return None, None, None


def move_up_left(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    x = i % w
    new_i = i - w - 1
    if y != 0 and x != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[new_i]
        puzzle[new_i] = temp
        return new_i, chr(new_i + 97), puzzle
    return None, None, None


def move_down(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    new_i = i + w
    if y != h - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[new_i]
        puzzle[new_i] = temp
        return new_i, chr(new_i + 97), puzzle
    return None, None, None


def move_down_right(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    x = i % w
    new_i = i + w + 1
    if y != h - 1 and x != w - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[new_i]
        puzzle[new_i] = temp
        return new_i, chr(new_i + 97), puzzle
    return None, None, None


def move_down_left(old_p, i, w, h):
    puzzle = old_p[:]
    y = i // w
    x = i % w
    new_i = i + w - 1
    if y != h - 1 and x != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[new_i]
        puzzle[new_i] = temp
        return new_i, chr(new_i + 97), puzzle
    return None, None, None


def move_right(old_p, i, w, h):
    puzzle = old_p[:]
    x = i % w
    new_i = i + 1
    if x != w - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[new_i]
        puzzle[new_i] = temp
        return new_i, chr(new_i + 97), puzzle
    return None, None, None


def move_left(old_p, i, w, h):
    puzzle = old_p[:]
    x = i % w
    new_i = i - 1
    if x != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[new_i]
        puzzle[new_i] = temp
        return new_i, chr(new_i + 97), puzzle
    return None, None, None
