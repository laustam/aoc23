from functools import reduce

file = open("input/day3", "r")


def is_number(x: int, y: int, matrix: [[chr]]) -> bool:
    inBounds: bool = x > - \
        1 and x < len(matrix[0]) and y > -1 and y < len(matrix)
    return inBounds and matrix[y][x].isnumeric()


# returns (number, ending_index of number)
def get_number(x: int, y: int, matrix: [[chr]]):
    while is_number(x, y, matrix):
        x -= 1
    x += 1

    num: int = 0
    while (is_number(x, y, matrix)):
        num = num * 10 + int(matrix[y][x])
        x += 1
    # x now points to the next non number
    return (num, x-1)


def find_numbers(x: int, y: int, matrix: [[chr]]) -> [int]:
    numbers: list = []

    # check left
    if (is_number(x-1, y, matrix)):
        num, _ = get_number(x-1, y, matrix)
        numbers.append(num)

    # check right
    if (is_number(x+1, y, matrix)):
        num, _ = get_number(x+1, y, matrix)
        numbers.append(num)

    # check above
    xi = x-1
    if (is_number(x-1, y-1, matrix)):
        num, xi = get_number(x-1, y-1, matrix)
        numbers.append(num)

    if (xi < x and is_number(x, y-1, matrix)):
        num, xi = get_number(x, y-1, matrix)
        numbers.append(num)

    if (xi < x and is_number(x+1, y-1, matrix)):
        num, xi = get_number(x+1, y-1, matrix)
        numbers.append(num)

    # check below
    xi = x-1
    if (is_number(x-1, y+1, matrix)):
        num, xi = get_number(x-1, y+1, matrix)
        numbers.append(num)

    if (xi < x and is_number(x, y+1, matrix)):
        num, xi = get_number(x, y+1, matrix)
        numbers.append(num)

    if (xi < x and is_number(x+1, y+1, matrix)):
        num, xi = get_number(x+1, y+1, matrix)
        numbers.append(num)

    return numbers


input_matrix: list[list[chr]] = []
for line in file:
    line_list: list[chr] = []
    for char in line.strip():
        line_list.append(char)

    input_matrix.append(line_list)

y: int = 0
gear_ratio: int = 0
while y < len(input_matrix):
    x: int = 0
    while x < len(input_matrix[0]):

        if input_matrix[y][x] != '*':
            x += 1
            continue

        # find numbers around gear
        gear_nums: [int] = find_numbers(x, y, input_matrix)
        if len(gear_nums) == 2:
            gear_ratio += reduce(lambda x, y: x*y, gear_nums)
        x += 1
    y += 1

print(gear_ratio)
