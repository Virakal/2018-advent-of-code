from aoc.claim import Claim


def d3_1(lines):
    claims = []

    for line in lines:
        claim = Claim.from_string(line)
        claims += claim.get_claimed_coords()

    claimed_coords = {}

    for coords in claims:
        if coords in claimed_coords:
            claimed_coords[coords] += 1
        else:
            claimed_coords[coords] = 1

    disputed_coords = [coords for coords,
                       num in claimed_coords.items() if num > 1]

    return len(disputed_coords)


def d3_2(lines):
    return 'NYI'


if __name__ == '__main__':
    with open('data/3.txt', 'r') as f:
        lines = list(f)

    print('Part 1:', d3_1(lines))
    print('Part 2:', d3_2(lines))
