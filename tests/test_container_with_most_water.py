import pytest
from solutions.container_with_most_water import max_area


def test_example_one():
    # Classic example: sticks at index 1 (height 8) and index 8 (height 7)
    # Distance = 7, min height = 7, water = 7 × 7 = 49
    # Validates the core two-pointer logic on a realistic input
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example_two():
    # Minimum possible input — only two sticks
    # Distance = 1, min height = 1, water = 1
    # Makes sure the solution handles the smallest valid case
    assert max_area([1, 1]) == 1


def test_wide_short():
    # The best container isn't always the tallest sticks
    # Outer sticks (height 1, distance 2) beat the taller middle stick
    # Water = 2 × 1 = 2 — tests that distance is factored in correctly
    assert max_area([1, 2, 1]) == 2


def test_increasing():
    # Heights increase left to right — pointer logic must not get greedy on height alone
    # Best container: indices 1 and 4 (height 2 and 5, distance 3, min = 2, water = 6)
    # Tests that the shorter pointer moves inward correctly
    assert max_area([1, 2, 3, 4, 5]) == 6


def test_all_equal():
    # All sticks are the same height — best container is always the widest
    # Distance = 3, height = 4, water = 4 × 3 = 12
    # Tests that the algorithm handles uniform input without getting confused
    assert max_area([4, 4, 4, 4]) == 12
