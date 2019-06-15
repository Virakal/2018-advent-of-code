from aoc.d3 import d3_1, d3_2


def test_d3_1_answer():
    with open('data/3.txt', 'r') as f:
        lines = list(f)

    assert d3_1(lines) == 114946


def test_d3_1_example_1():
    lines = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ]

    assert d3_1(lines) == 4
