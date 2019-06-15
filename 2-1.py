with open('2-1.txt', 'r') as f:
    lines = list(f)

has2 = 0
has3 = 0

for line in lines:
    counts = {}

    for char in line:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    if 2 in counts.values():
        has2 += 1

    if 3 in counts.values():
        has3 += 1

print(has2 * has3)
