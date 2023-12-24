file = open("input/day14", "r")

lines = file.read().splitlines()
TOTAL_ROWS = len(lines)
TOTAL_COLS = len(lines[0])

total_load = 0

for x in range(TOTAL_COLS):
    rounded_rocks = 0
    row_start = TOTAL_ROWS
    for y,line in enumerate(lines):
        row_num = TOTAL_ROWS-y

        if lines[y][x] == 'O':
            rounded_rocks+=1

        elif lines[y][x] == '#':
            for rock in range(rounded_rocks):
                total_load += row_start
                row_start -= 1

            # update
            row_start = row_num-1
            rounded_rocks = 0
    
    for _ in range(rounded_rocks):
        total_load += row_start
        row_start -= 1
    
print(total_load)