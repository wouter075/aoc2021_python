import math

with open('day13.txt') as f:
    lines = [line.rstrip() for line in f]

coords = []
folds = []

# parse input
for line in lines:
    if "," in line:
        x = line.split(',')[0]
        y = line.split(',')[1]
        coords.append([int(x), int(y)])
    if "=" in line:
        d = line.split(" ")[2].split("=")[0]
        n = int(line.split(" ")[2].split("=")[1])
        folds.append([d, n])

# max values:
maxX = max(coords, key=lambda x: x[0])[0] + 1
maxY = max(coords, key=lambda x: x[1])[1] + 1

# build the grid
grid = []
for y in range(maxY):
    row = []
    for x in range(maxX):
        row.append('.')
    grid.append(row)

# build grid:
for x, y in coords:
    grid[y][x] = "#"

# folding time!
# part 1: for d, n in folds[:1]:
for d, n in folds:
    if d == 'y':
        start_y = math.ceil(len(grid) / 2)
        for liner in range(start_y, len(grid)):
            m = (n * 2) - liner
            for c in range(len(grid[0])):
                if grid[liner][c] == "#":
                    grid[m][c] = grid[liner][c]
        # remove line
        for liner in range(len(grid) - 1, start_y - 2, -1):
            grid.pop(liner)

    if d == 'x':
        start_x = math.ceil(len(grid[0]) / 2)
        for cols in range(start_x, len(grid[0])):
            m = (n * 2) - cols
            for c in range(len(grid)):
                if grid[c][cols] == "#":
                    grid[c][m] = grid[c][cols]
        # remove col
        for cols in range(len(grid[0]) - 1, n - 1, -1):
            # print(cols)
            for r in range(len(grid) - 1, -1, -1):
                grid[r].pop(cols)

part1 = 0
for y in range(len(grid)):
    print(grid[y])
    for x in range(len(grid[0])):
        if grid[y][x] == "#":
            part1 += 1

print(f"Part 1: {part1}")



