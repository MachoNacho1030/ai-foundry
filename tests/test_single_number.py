import pytest
from solutions.single_number import single_number


# --- Examples directly from the problem statement ---

def test_example_one():
    # [2,2,1] — the 2s pair up, 1 is alone
    assert single_number([2, 2, 1]) == 1

def test_example_two():
    # [4,1,2,1,2] — 1s and 2s pair up, 4 is alone
    assert single_number([4, 1, 2, 1, 2]) == 4

def test_example_three():
    # single element array — it is always the answer
    assert single_number([1]) == 1


# --- Position of the single element ---

def test_single_at_start():
    # unpaired element is first in the array
    assert single_number([7, 3, 3]) == 7

def test_single_in_middle():
    # unpaired element is sandwiched between pairs
    assert single_number([1, 1, 9, 2, 2]) == 9

def test_single_at_end():
    # unpaired element is last in the array
    assert single_number([4, 4, 5]) == 5


# --- Negative numbers ---

def test_negative_single():
    # the unpaired element is a negative number
    assert single_number([-1, 2, 2]) == -1

def test_all_negative_pairs_one_positive():
    # pairs are negative, lone element is positive
    assert single_number([-3, -3, 5]) == 5


# --- Large input (performance) ---

def test_large_input():
    # build a big array of pairs, append one lone element at the end
    # XOR must handle 30000 elements in linear time
    nums = []
    for i in range(1, 15001):
        nums.append(i)
        nums.append(i)
    nums.append(99999)  # the single unpaired element
    assert single_number(nums) == 99999
