with open('day8.txt') as f:
    lines = [line.rstrip() for line in f]

segments = []
signals = []
known_len = {2, 3, 4, 7}
part1 = 0


for line in lines:
    parts = line.split(" | ")
    segments.append(parts[0])
    signals.append(parts[1])

for signal in signals:
    for p in signal.split(" "):
        if len(p) in known_len:
            part1 += 1

# part 2
for segment in segments:
    unknown = []
    for p in segment.split(" "):
        if len(p) not in known_len:
            unknown.append("".join(sorted(p)))
            # print("".join(sorted(p)))
            if len(p) == 5:
                # 2, 3, 5<
                # if there are 3 the same parts in the other string, its 5
                # https://www.w3schools.com/python/trypython.asp?filename=demo_ref_set_intersection
                sort = "".join(sorted(p))
                print(sort)
    print()



print(f'Part 1: {part1}')
