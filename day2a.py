with open('day2.txt') as f:
    lines = [line.rstrip() for line in f]

hor = 0
depth = 0
for x in range(len(lines)):
    d, m = lines[x].split(" ")
    m = int(m)
    if d == "forward":
        depth += m
    if d == "down":
        hor += m
    if d == "up":
        hor -= m

print(f"Part 1: {int(hor) * int(depth)}")


