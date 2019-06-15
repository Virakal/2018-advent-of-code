from aoc.d1 import d1_1, d1_2
import pytest


@pytest.fixture
def filedata():
    with open('data/1.txt', 'r') as f:
        return list(f)


def test_d1_1_answer(filedata):
    assert d1_1(filedata) == 423


def test_d1_1_example_1():
    lines = ['+1', '+1', '+1']
    assert d1_1(lines) == 3


def test_d1_1_example_2():
    lines = ['+1', '+1', '-2']
    assert d1_1(lines) == 0


def test_d1_1_example_3():
    lines = ['-1', '-2', '-3']
    assert d1_1(lines) == -6


def test_d1_2_answer(filedata):
    assert d1_2(filedata) == 61126


def test_d1_2_example_1():
    lines = ['+1', '-1']
    assert d1_2(lines) == 0


def test_d1_2_example_2():
    lines = ['+3', '+3', '+4', '-2', '-4']
    assert d1_2(lines) == 10


def test_d1_2_example_3():
    lines = ['-6', '+3', '+8', '+5', '-6']
    assert d1_2(lines) == 5


def test_d1_2_example_4():
    lines = ['+7', '+7', '-2', '-7', '-4']
    assert d1_2(lines) == 14
