from aoc.d1 import d1_1, d1_2


def test_file_d1_1():
    with open('data/1.txt', 'r') as f:
        lines = list(f)

    assert d1_1(lines) == 423


def test_file_d1_2():
    with open('data/1.txt', 'r') as f:
        lines = list(f)

    assert d1_2(lines) == 61126
