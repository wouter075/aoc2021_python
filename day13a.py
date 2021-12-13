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
    # print(f'{y}, {x}')
    grid[y][x] = "#"


# folding time!
for d, n in folds:
    # print(f'{d}: {n}')
    if d == 'y':
        start_y = math.ceil(len(grid) / 2)
        for l in range(start_y, len(grid)):
            m = (n * 2) - l
            for c in range(maxY):
                print(f'{c},{l} - {c},{m}')
                # grid[m][c] = grid[l][c]

            print("-"*10)






# print
for y in range(len(grid)):
    print(grid[y])

