import pytest
from solutions.two_sum import two_sum


# --- Standard cases ---

def test_example_one():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_example_two():
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_example_three():
    # duplicate values — both point to different indices
    assert two_sum([3, 3], 6) == [0, 1]


# --- Middle elements ---

def test_answer_not_at_start():
    # 3 + 8 = 11, at indices 2 and 3
    assert two_sum([1, 5, 3, 8, 2], 11) == [2, 3]


# --- Negative numbers ---

def test_negative_numbers():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]

def test_both_negative():
    # -2 + (-1) = -3, at indices 1 and 2
    assert two_sum([-5, -2, -1, 0], -3) == [1, 2]


# --- Two-element array ---

def test_minimum_array_size():
    assert two_sum([1, 9], 10) == [0, 1]


# --- Large input (performance) ---

def test_large_input():
    n = 10_000
    nums = list(range(n))
    # last two elements sum to the target
    target = (n - 1) + (n - 2)
    result = two_sum(nums, target)
    assert set(result) == {n - 1, n - 2}
