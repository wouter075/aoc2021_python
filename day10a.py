with open('day10.txt') as f:
    lines = [line.rstrip() for line in f]

couples = {'[]', '{}', '()', '<>'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
points2 = {'(': 1, '[': 2, '{': 3, '<': 4}
part1 = 0
scores = []


def remove_couples(line):
    while any(couple in line for couple in couples):
        for couple in couples:
            line = line.replace(couple, "")
    return line


def check_corrupted(line):
    # a corrupted line is a line with still a couple in it:
    counts = {e: line.count(e) for e in set(line)}
    for couple in couples:
        if couple[0] in counts and couple[1] in counts:
            return True
    return False


for line in lines:
    line2 = remove_couples(line)
    if check_corrupted(line2):
        for char in line2:
            if char in points:
                part1 += points[char]
                break
    else:
        score = 0
        for part in line2[::-1]:
            score = score * 5
            score += points2[part]
        scores.append(score)

# sorting for part 2:
scores.sort()
i = int((len(scores)) / 2)

print(f"Part 1: {part1}")
print(f"Part 2: {scores[i]}")
