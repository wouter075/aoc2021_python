with open('day2.txt') as f:
    lines = [line.rstrip() for line in f]

hor, depth, aim = 0, 0, 0
for x in range(len(lines)):
    d, m = lines[x].split(" ")
    m = int(m)
    if d == "forward":
        hor += int(m)
        depth += m * aim
    if d == "down":
        aim += int(m)
    if d == "up":
        aim -= int(m)
print(f"Part 2: {int(hor) * int(depth)}")
