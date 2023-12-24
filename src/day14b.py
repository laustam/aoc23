import copy

file = open("input/day14", "r")

lines = [list(line) for line in file.read().splitlines()] # transform str -> list (str is immutable)

TOTAL_ROWS = len(lines)
TOTAL_COLS = len(lines[0])
TOTAL_CYCLES = 1000000000

def horizontal_shift(lines, y_range):  # y range specifies whether shift north or south
    for x in range(TOTAL_COLS):
        empty_spaces = []  # contains y coords of empty spaces, used as a queue
        for y in y_range:
            match lines[y][x]:
                case 'O':
                    if empty_spaces:
                        new_y = empty_spaces.pop(0)  # dequeue
                        # from old -> new spot
                        lines[new_y][x] = 'O'
                        lines[y][x] = '.'
                        # add old spot to empty spaces queue
                        empty_spaces.append(y)

                case '.':
                    empty_spaces.append(y)

                case '#':
                    empty_spaces = []

def vertical_shift(lines, x_range):  # x range specifies whether shift west or east
    for y in range(TOTAL_ROWS):
        empty_spaces = []  # contains y coords of empty spaces, used as a queue
        for x in x_range:
            match lines[y][x]:
                case 'O':
                    if empty_spaces:
                        new_x = empty_spaces.pop(0)  # dequeue
                        # from old -> new spot
                        lines[y][new_x] = 'O'
                        lines[y][x] = '.'
                        # add old spot to empty spaces queue
                        empty_spaces.append(x)

                case '.':
                    empty_spaces.append(x)

                case '#':
                    empty_spaces = []


def total_load(lines):
    total_load = 0
    for y in range(TOTAL_COLS):
        for x in range(TOTAL_ROWS):
            row_num = TOTAL_ROWS-y

            if lines[y][x] == 'O':
                total_load += row_num

    return total_load


seen_grid_cycles = []

for _ in range(TOTAL_CYCLES):
    horizontal_shift(lines, range(TOTAL_ROWS))  # north
    vertical_shift(lines, range(TOTAL_COLS))  # west
    horizontal_shift(lines, range(TOTAL_ROWS-1, -1, -1))  # south
    vertical_shift(lines, range(TOTAL_COLS-1, -1, -1))  # east

    if lines in seen_grid_cycles:
        cycle_start = seen_grid_cycles.index(lines)
        seen_grid_cycles = seen_grid_cycles[cycle_start:]
        break

    seen_grid_cycles.append(copy.deepcopy(lines))

last_cycle_idx = (TOTAL_CYCLES-cycle_start) % len(seen_grid_cycles) - 1
last_cycle = seen_grid_cycles[last_cycle_idx]

print(total_load(last_cycle))