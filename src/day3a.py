file = open("input/day3", "r")


def isSymbol(x, y, matrix) -> bool:
    inBounds: bool = x > -1 and x < len(matrix[0]) and y > -1 and y < len(matrix)
    return inBounds and matrix[y][x] != '.' and not matrix[y][x].isnumeric()


def symbolInRange(coord_range: [(int, int)], matrix: [[chr]]) -> bool:
    min_x, min_y = coord_range[0]
    max_x, max_y = coord_range[-1]

    # check left and right
    if isSymbol(min_x-1, min_y, matrix) or isSymbol(max_x+1, max_y, matrix):
        return True

    # check above and below
    for x, y in coord_range:
        if isSymbol(x, y-1, matrix) or isSymbol(x, y+1, matrix):
            return True

    # check left diagonal
    if isSymbol(min_x-1, min_y-1, matrix) or isSymbol(min_x-1, min_y+1, matrix):
        return True

    # check right diagonal
    if isSymbol(max_x+1, max_y-1, matrix) or isSymbol(max_x+1, max_y+1, matrix):
        return True

    return False


input_matrix: list[list[chr]] = []
for line in file:
    line_list: list[chr] = []
    for char in line.strip():
        line_list.append(char)

    input_matrix.append(line_list)

part_numbers: [int] = []
y: int = 0
while y < len(input_matrix):
    x: int = 0
    while x < len(input_matrix[0]):

        curr_num: int = 0
        coord_range: (int, int) = []

        if not input_matrix[y][x].isnumeric():
            x += 1
            continue

        # locate full number
        while x < len(input_matrix[0]) and input_matrix[y][x].isnumeric():
            curr_num = curr_num * 10 + int(input_matrix[y][x])
            coord_range.append((x, y))
            x += 1

        # check if symbol is in range
        if symbolInRange(coord_range=coord_range, matrix=input_matrix):
            part_numbers.append(curr_num)
    y += 1

print(sum(part_numbers))