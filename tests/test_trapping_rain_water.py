"""
Tests for Trapping Rain Water (LeetCode #42)
Written FIRST — before any solution exists. This is TDD.
"""
import pytest
import sys
import os

# Add solutions directory to path so we can import the solution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))

from trapping_rain_water import trap


# --- Core examples from the problem statement ---

def test_leetcode_example_one():
    # Standard example: 6 units of water trapped across a varied elevation
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_leetcode_example_two():
    # Simpler example: large walls on both ends trap 9 units
    assert trap([4, 2, 0, 3, 2, 5]) == 9


# --- Edge cases: no water can be trapped ---

def test_empty_array():
    # No bars at all — nothing to trap
    assert trap([]) == 0


def test_single_element():
    # One bar has no neighbors — can't trap water
    assert trap([5]) == 0


def test_two_elements():
    # Two bars, no middle — no water possible
    assert trap([3, 4]) == 0


def test_strictly_increasing():
    # Water always flows off the right side — nothing trapped
    assert trap([1, 2, 3, 4, 5]) == 0


def test_strictly_decreasing():
    # Water always flows off the left side — nothing trapped
    assert trap([5, 4, 3, 2, 1]) == 0


def test_all_same_height():
    # Flat surface — no valleys to fill
    assert trap([3, 3, 3, 3]) == 0


# --- Simple trap cases ---

def test_single_valley():
    # Classic valley: walls of height 2 on each side, depth 1 in middle
    # Water trapped = min(2,2) - 0 = 2
    assert trap([2, 0, 2]) == 2


def test_asymmetric_walls():
    # Left wall is taller — water level limited by the shorter right wall
    # [3, 0, 1] → min(3,1) - 0 = 1 unit trapped at index 1
    assert trap([3, 0, 1]) == 1


def test_wide_valley():
    # Wide flat bottom between two walls
    # [3, 0, 0, 0, 3] → 3 units trapped across three positions
    assert trap([3, 0, 0, 0, 3]) == 9


# --- Constraints boundary ---

def test_all_zeros():
    # All flat at zero — no walls, nothing trapped
    assert trap([0, 0, 0, 0]) == 0


def test_one_tall_bar_in_middle():
    # Tall bar in the middle, low bars on sides — water flows off
    assert trap([1, 3, 1]) == 0
