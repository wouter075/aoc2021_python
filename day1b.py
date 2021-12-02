with open('day1.txt') as f:
    lines = [int(line.rstrip()) for line in f]

# part 2
c = 0
for x in range(len(lines) - 3):
    if lines[x] + lines[x + 1] + lines[x + 2] < lines[x + 1] + lines[x + 2] + lines[x + 3]:
        c += 1

print(f"Part 2: {c}")
