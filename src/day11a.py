file = open("input/day11", "r")

lines = file.read().splitlines() # splitlines removes the \n! (compared to readlines)

GALAXY_EXPANSION_CONSTANT = 1

def expand_universe(universe: list[list[chr]]) -> (set[int], set[int]): # returns two sets containing rows and cols affected by expansion
    # find rows to expand
    expanded_rows: set[int] = set()
    for row in range(len(universe)):
        if '#' not in universe[row]:
            expanded_rows.add(row)

    # find cols to expand
    expanded_cols: set[int] = set()
    for col in range(len(universe[0])):
        expand_col: bool = True
        for row in range(len(universe)):
            if universe[row][col] == '#':
                expand_col = False
                break

        if expand_col:
            expanded_cols.add(col)

    return(expanded_cols, expanded_rows)

def find_galaxies(universe: list[list[chr]]) -> list[tuple[int,int]]:
    galaxies: list[tuple[int,int]] = []
    for y, row  in enumerate(universe):
        for x, cell in enumerate(row):
            if cell == '#':
                galaxies.append((x,y))

    return galaxies

def shortest_dist(expansions: (set[int], set[int]), galaxy1: tuple[int,int], galaxy2: tuple[int,int]):
    x1, y1 = galaxy1
    x2, y2 = galaxy2
    expanded_x, expanded_y = expansions
    nr_expanded_cells = (len(set(range(min(x1,x2), max(x1,x2))).intersection(expanded_x)) +
                         len(set(range(min(y1,y2), max(y1,y2))).intersection(expanded_y)))
    return nr_expanded_cells * GALAXY_EXPANSION_CONSTANT + abs(x1-x2) + abs(y1-y2)

expansions = expand_universe(lines)
galaxies = find_galaxies(lines)

sum_shortest_paths: int = 0
for idx1, galaxy1 in enumerate(galaxies):
    for idx2, galaxy2 in enumerate(galaxies[idx1+1:],start=idx1):
        sum_shortest_paths += shortest_dist(expansions, galaxy1, galaxy2)

print(sum_shortest_paths)