from aoc.d2 import d2_1, d2_2
import pytest


@pytest.fixture
def filedata():
    with open('data/2.txt', 'r') as f:
        return list(f)


def test_d2_1_answer(filedata):
    assert d2_1(filedata) == 7470


def test_d2_1_example_1():
    lines = [
        'abcdef',
        'bababc',
        'abbcde',
        'abcccd',
        'aabcdd',
        'abcdee',
        'ababab',
    ]

    assert d2_1(lines) == 12


def test_d2_2_answer(filedata):
    assert d2_2(filedata) == 'kqzxdenujwcstybmgvyiofrrd'


def test_d2_2_example_1():
    lines = [
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz',
    ]

    assert d2_2(lines) == 'fgij'
