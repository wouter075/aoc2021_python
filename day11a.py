from collections import deque

with open('day11.txt') as f:
    lines = [line.rstrip() for line in f]

# create grid
grid = list(map(list, lines))
flashed = 0

for _ in range(3):
    # update the grid:
    grid = [[int(f) + 1 for f in line] for line in grid]

    # check grid for 10's add them to the list
    flash_list = []
    for l in range(len(grid)):
        line = grid[l]
        for c in line:
            if c > 9:
                flash_list.append({l, c})

    while len(flash_list):
        flashed += 1



    print(flash_list)

