def move_up(puzzle, i, w):
    y = i / w
    if y != 0:
        i -= w

def move_down(puzzle, i, w, h):
    y = i / w
    if y != h - 1:
        i += w

def move_right(puzzle, i, w, h):
    x = i % w
    if x != w - 1:
        i += 1

def move_left(puzzle, i, w, h):
    x = i % w
    if x != 0:
        i -= 1