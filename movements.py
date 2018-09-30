def move_up(puzzle, i, w, h):
    y = i // w
    if y != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[i - w]
        puzzle[i - w] = temp
        return puzzle[i - w], puzzle
    return None


def move_up_right(puzzle, i, w, h):
    y = i // w
    x = i % w
    if y != 0 and x != w - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[i + 1 + w]
        puzzle[i + 1 + w] = temp
        return puzzle
    return None


def move_up_left(puzzle, i, w, h):
    y = i // w
    x = i % w
    if y != 0 and x != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[i - 1 + w]
        puzzle[i - 1 + w] = temp
        return puzzle
    return None


def move_down(puzzle, i, w, h):
    y = i // w
    if y != h - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[i + w]
        puzzle[i + w] = temp
        return puzzle
    return None


def move_down_right(puzzle, i, w, h):
    y = i // w
    x = i % w
    if y != h - 1 and x != w - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[i + 1 + w]
        puzzle[i + 1 + w] = temp
        return puzzle
    return None


def move_down_left(puzzle, i, w, h):
    y = i // w
    x = i % w
    if y != h - 1 and x != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[i + w - 1]
        puzzle[i + w - 1] = temp
        return puzzle
    return None


def move_right(puzzle, i, w, h):
    x = i % w
    if x != w - 1:
        temp = puzzle[i]
        puzzle[i] = puzzle[i + 1]
        puzzle[i + 1] = temp
        return puzzle
    return None


def move_left(puzzle, i, w, h):
    x = i % w
    if x != 0:
        temp = puzzle[i]
        puzzle[i] = puzzle[i - 1]
        puzzle[i - 1] = temp
        return puzzle
    return None
