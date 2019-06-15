from aoc.d3 import d3_1, d3_2
import pytest


@pytest.fixture
def filedata():
    with open('data/3.txt', 'r') as f:
        return list(f)


def test_d3_1_answer(filedata):
    assert d3_1(filedata) == 114946


def test_d3_1_example_1():
    lines = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ]

    assert d3_1(lines) == 4


def test_d3_2_answer(filedata):
    assert d3_2(filedata) == 877


def test_d3_2_example_1():
    lines = [
        '#1 @ 1,3: 4x4',
        '#2 @ 3,1: 4x4',
        '#3 @ 5,5: 2x2',
    ]

    assert d3_2(lines) == 3
