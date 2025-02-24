from aoc.d4 import d4_1, d4_2
import pytest


@pytest.fixture
def filedata():
    with open('data/4.txt', 'r') as f:
        return list(f)


def test_d4_1_answer(filedata):
    assert d4_1(filedata) == '?'


def test_d4_exmaple_1():
    lines = [
        '[1518-11-01 00:00] Guard #10 begins shift',
        '[1518-11-01 00:05] falls asleep',
        '[1518-11-01 00:25] wakes up',
        '[1518-11-01 00:30] falls asleep',
        '[1518-11-01 00:55] wakes up',
        '[1518-11-01 23:58] Guard #99 begins shift',
        '[1518-11-02 00:40] falls asleep',
        '[1518-11-02 00:50] wakes up',
        '[1518-11-03 00:05] Guard #10 begins shift',
        '[1518-11-03 00:24] falls asleep',
        '[1518-11-03 00:29] wakes up',
        '[1518-11-04 00:02] Guard #99 begins shift',
        '[1518-11-04 00:36] falls asleep',
        '[1518-11-04 00:46] wakes up',
        '[1518-11-05 00:03] Guard #99 begins shift',
        '[1518-11-05 00:45] falls asleep',
        '[1518-11-05 00:55] wakes up',
    ]

    assert d4_1(lines) == 240


def test_d4_2_answer(filedata):
    assert d4_1(filedata) == '?'
