def try_combo(x, y):
    x = x.strip()
    y = y.strip()

    diff = 0
    common = []

    for i in range(len(x)):
        if x[i] == y[i]:
            common += x[i]
        else:
            diff += 1

    if diff == 1:
        return ''.join(common)


def d2_1(lines):
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

    return has2 * has3


def d2_2(lines):
    for line1 in lines:
        for line2 in lines:
            x = try_combo(line1, line2)

            if x:
                return x


if __name__ == '__main__':
    with open('data/2.txt', 'r') as f:
        lines = list(f)

    print('Part 1:', d2_1(lines))
    print('Part 2:', d2_2(lines))
