import re


class Claim:
    string_re = re.compile(
        r'^#(?P<id>\d+) @ (?P<start_x>\d+),(?P<start_y>\d+): (?P<h_size>\d+)x(?P<v_size>\d+)$')

    def __init__(self, id: int, start_x: int, start_y: int, h_size: int,
                 v_size: int):
        self.id = id
        self.start_x = start_x
        self.start_y = start_y
        self.h_size = h_size
        self.v_size = v_size

    @classmethod
    def from_string(cls, string: str):
        m = cls.string_re.search(string)

        return cls(int(m.group('id')),
                   int(m.group('start_x')),
                   int(m.group('start_y')),
                   int(m.group('h_size')),
                   int(m.group('v_size'))
                   )

    def get_claimed_coords(self):
        coords = []

        for x in range(self.start_x, self.start_x + self.h_size):
            for y in range(self.start_y, self.start_y + self.v_size):
                coords.append((x, y))

        return coords


with open('3.txt', 'r') as f:
    lines = list(f)

# Debug
# lines = [
#     "#1 @ 1,3: 4x4",
#     "#2 @ 3,1: 4x4",
#     "#3 @ 5,5: 2x2",
# ]

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

disputed_coords = [coords for coords, num in claimed_coords.items() if num > 1]

print(len(disputed_coords))
