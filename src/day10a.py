file = open("input/day10", "r")

grid: list[str] = file.readlines()

# find start S location
row: int = 0
col: int = 0
found_S: bool = False
S: tuple[int, int] = (0,0)
for row in range(len(grid)):
    for col in range(len(grid[0])):
        tile: chr = grid[row][col].strip()
        if tile == 'S':
            found_S = True
            S = (col, row)
            break
    if found_S:
        break

# define different possible steps
up_tiles: list[chr] = ['|', 'F', '7']
left_tiles: list[chr] = ['-', 'F', 'L']
right_tiles: list[chr] = ['-', '7', 'J']
down_tiles: list[chr] = ['|', 'J', 'L']

valid_move: dict = {
    # dir : source tile that can move in given dir
    (0,-1) : ['S', '|', 'L', 'J'], #up
    (-1,0) : ['S', '7', '-', 'J'], #left
    (+1,0) : ['S', 'F', '-', 'L'], #right
    (0,+1) : ['S', '|', 'F', '7'] #down
}

def at(grid: list[str], pos: tuple[int,int]) -> chr: return grid[pos[1]][pos[0]]
def move(pos: tuple[int,int], dir: tuple[int,int]) -> tuple[int, int]: return (pos[0] + dir[0], pos[1] + dir[1])
def inbounds(grid: list[str], pos: tuple[int,int]) -> bool: return pos[1] >= 0 and pos[0] >= 0 and pos[1] < len(grid) and pos[0] < len(grid[0])
def can_move(curr_pos: tuple[int,int], dir: tuple[int,int], prev_pos: tuple[int,int], valid_tiles: list[chr]) -> bool:
    new_pos: tuple[int,int] = move(curr_pos, dir)
    return at(grid, curr_pos) in valid_move.get(dir) and new_pos != prev_pos and inbounds(grid, new_pos) and at(grid, new_pos) in valid_tiles

# count nr of nodes in loop
loop_nodes: int = 0
prev_pos: tuple[int,int] = (-1,-1)
curr_pos: tuple[int,int] = S

while True:
    loop_nodes += 1
    if can_move(curr_pos, (0,-1), prev_pos, up_tiles):
        prev_pos = curr_pos
        curr_pos = move(curr_pos, (0,-1))

    elif can_move(curr_pos, (-1,0), prev_pos, left_tiles):
        prev_pos = curr_pos
        curr_pos = move(curr_pos, (-1,0))

    elif can_move(curr_pos, (+1,0), prev_pos, right_tiles):
        prev_pos = curr_pos
        curr_pos = move(curr_pos, (+1,0))

    elif can_move(curr_pos, (0,+1), prev_pos, down_tiles):
        prev_pos = curr_pos
        curr_pos = move(curr_pos, (0,+1))

    else: # back at S
        break

print(int(loop_nodes/2))