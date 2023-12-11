file = open("input/day10", "r")

grid: list[str] = file.readlines()

    # define different possible steps
up_tiles: list[chr] = ['|', 'F', '7']
left_tiles: list[chr] = ['-', 'F', 'L']
right_tiles: list[chr] = ['-', '7', 'J']
down_tiles: list[chr] = ['|', 'J', 'L']

# get tiles in cycle
def get_cycle_tiles(grid: list[str]) -> dict:
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

    prev_pos: tuple[int,int] = (-1,-1)
    curr_pos: tuple[int,int] = S
    tiles_in_cycle: dict = {S : 'S'} # maps coord to type of tile

    while True:
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
        
        tiles_in_cycle[curr_pos] = at(grid, curr_pos)
    
    return tiles_in_cycle

cycle_tiles: dict = get_cycle_tiles(grid)

# find candidate points
candidate_points: list[tuple[int,int]] = []

for row in range(len(grid)):
    for col in range(len(grid[0].strip())): # strip to remove \n at end
        if (col,row) not in cycle_tiles.keys():
            candidate_points.append((col,row)) # very inefficient damn

# send upwards ray through shape and find nr of intersections
inner_points: int = 0
for point in candidate_points:
    print("candidate: {}".format(point))

    # find intersecting points
    (x,y) = point[0], point[1]-1
    intersects: list[chr] = []

    while y >= 0:
        if (x,y) in cycle_tiles.keys() and cycle_tiles[(x,y)] != '|': # need to exclude | characters from consideration
            
            if cycle_tiles[(x,y)] != 'S':
                intersects.append(cycle_tiles[(x,y)])

            # if intersect with S, determine the "direction" of S by checking what it's connected to
            # (dont need to check above because we don't consider |)

            # check left
            elif cycle_tiles.get((x-1,y)) in left_tiles:
                intersects.append('7') # S acts as 7

            # check right
            elif cycle_tiles.get((x+1,y)) in right_tiles:
                intersects.append('F') # S acts as F

        y-=1

    # count nr of intersections    
    nr_intersects: int = 0
    i: int = 0
    while i < len(intersects):
        # horizontal crossing lines are counted normally
        if intersects[i] == '-' or intersects[i+1] == '-':
            nr_intersects += 1
            i+=1

        # count once: combos of FJ and 7L
        elif (i+1 >= len(intersects) or
            intersects[i] == 'F' and intersects[i+1] == 'J' or
            intersects[i] == 'J' and intersects[i+1] == 'F' or
            intersects[i] == '7' and intersects[i+1] == 'L' or
            intersects[i] == 'L' and intersects[i+1] == '7'):

            nr_intersects += 1
            i+=2

        # count twice: combos of FL and 7J
        else:
            nr_intersects += 2
            i+=2

    # odd number of intersects means that is is a inner point!
    if nr_intersects % 2 != 0:
        inner_points += 1

print(inner_points)