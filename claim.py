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
