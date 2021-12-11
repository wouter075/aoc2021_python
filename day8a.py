with open('day8.txt') as f:
    lines = [line.rstrip() for line in f]

segments = []
signals = []
known_len = {2, 3, 4, 7}
part1 = 0
part2 = 0

for line in lines:
    parts = line.split(" | ")
    segments.append(parts[0])
    signals.append(parts[1])

for signal in signals:
    for p in signal.split(" "):
        if len(p) in known_len:
            part1 += 1

# part 2
for i in range(len(segments)):
    segment = segments[i]
    signal = signals[i]
    unknown = []
    words = {}
    known = {}

    for i in range(10):
        known[i] = {}
        words[i] = {}

    for p in segment.split(" "):
        if len(p) == 2:
            known[1] = "".join(sorted(p))
        if len(p) == 3:
            known[7] = "".join(sorted(p))
        if len(p) == 4:
            known[4] = "".join(sorted(p))
        if len(p) == 7:
            known[8] = "".join(sorted(p))

        else:
            unknown.append("".join(sorted(p)))

    u2 = unknown
    for u in range(10):
        if len(known[u]) > 0:
            try:
                u2.remove(known[u])
            except ValueError:
                pass

    while len(u2) is not 0:
        for p in unknown:
            if len(p) == 5:
                # 2
                if len(set(p).intersection(known[4])) == 2:
                    known[2] = "".join(sorted(p))
                    u2.remove(p)
                # 3
                if len(set(p).intersection(known[1])) == 2:
                    known[3] = "".join(sorted(p))
                    u2.remove(p)
                # 5
                if len(known[3]) > 0:
                    if len(set(p).intersection(known[3])) == 4:
                        known[5] = "".join(sorted(p))
                        try:
                            u2.remove(p)
                        except ValueError:
                            continue
            if len(p) == 6:
                # 6
                if len(set(p).intersection(known[1])) == 1:
                    known[6] = "".join(sorted(p))
                    u2.remove(p)
                # 9
                if len(set(p).intersection(known[4])) == 4:
                    known[9] = "".join(sorted(p))
                    u2.remove(p)

        if len(u2) == 1:
            known[0] = u2[0]
            u2.remove(u2[0])
    print(known)
    # we know all the segments!
    sum = ""
    print(signal)
    for s in signal.split(" "):
        s = "".join(sorted(s))
        sum += str(list(known.keys())[list(known.values()).index(s)])
    part2 += int(sum)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
