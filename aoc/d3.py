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
    claims = {}

    # Build claims
    for line in lines:
        claim = Claim.from_string(line)
        claims[claim.id] = claim.get_claimed_coords()

    # Work out claims per coord
    claimed_coords = {}

    for id in claims:
        coords_list = claims[id]

        for coords in coords_list:
            if coords in claimed_coords:
                claimed_coords[coords].append(id)
            else:
                claimed_coords[coords] = [id]

    # Find coords with only one claim
    undisputed_coords = set(
        coords for coords in claimed_coords if len(claimed_coords[coords]) == 1)

    # Find a claim where every coord is undisputed
    for id in claims:
        correct = True
        for coords in claims[id]:
            if coords not in undisputed_coords:
                correct = False
                break

        if correct:
            return id


if __name__ == '__main__':
    with open('data/3.txt', 'r') as f:
        lines = list(f)

    print('Part 1:', d3_1(lines))
    print('Part 2:', d3_2(lines))
