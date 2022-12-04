from collections import Counter
import numpy as np
from copy import deepcopy


def neighbor_check(index, grid):
    neighbors = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    y_max = len(grid)
    x_max = len(grid[0])
    n_of_lit_lights = 0
    for dy, dx in neighbors:
        neighbor_y = index[0] + dy
        neighbor_x = index[1] + dx
        if not ((0 <= neighbor_y < y_max) and (0 <= neighbor_x < x_max)):
            continue
        if grid[neighbor_y][neighbor_x] == '#':
            n_of_lit_lights += 1
    if index in [(0, 0), (99, 99), (0, 99), (99, 0)]:  # Part B
        return 2
    return n_of_lit_lights


with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]

grid = []
for row in data:
    grid.append([x for x in row])

for _ in range(100):
    new_grid = deepcopy(grid)
    for row_num, row in enumerate(grid):
        for col_num, elem in enumerate(row):
            index = (row_num, col_num)
            neighbor_lights = neighbor_check(index, grid)
            if elem == "#":
                lit = True
            else:
                lit = False

            if lit and neighbor_lights in [2, 3]:
                continue
            elif lit:
                new_grid[row_num][col_num] = "."
            elif not lit and (neighbor_lights == 3):
                new_grid[row_num][col_num] = "#"

    grid = new_grid
check_grid = np.array(grid)
answer = dict(Counter(check_grid.flatten()))
print(answer["#"])



