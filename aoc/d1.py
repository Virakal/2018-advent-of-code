def d1_1(lines):
    return sum(int(line) for line in lines)


def d1_2(lines):
    hit = {}
    a = 0

    while True:
        for line in lines:
            hit[a] = True

            a += int(line)

            if a in hit:
                return a


if __name__ == '__main__':
    with open('data/1.txt', 'r') as f:
        lines = list(f)

    print('Part 1:', d1_1(lines))
    print('Part 2:', d1_2(lines))
