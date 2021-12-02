with open('day1.txt') as f:
    lines = [int(line.rstrip()) for line in f]

c = 0
# part 1
for x in range(len(lines) - 1):
    if lines[x] < lines[x + 1]:
        c += 1


print(f"Part 1: {c}")
