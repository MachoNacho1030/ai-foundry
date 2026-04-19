import pytest
from solutions.median_two_sorted_arrays import find_median_sorted_arrays


# --- Basic cases ---

def test_odd_total_length():
    # merged = [1, 2, 3], median = 2.0
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0

def test_even_total_length():
    # merged = [1, 2, 3, 4], median = (2+3)/2 = 2.5
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5


# --- Edge cases ---

def test_one_empty_array_odd():
    # nums1 is empty, median of [1, 2, 3]
    assert find_median_sorted_arrays([], [1, 2, 3]) == 2.0

def test_one_empty_array_even():
    # nums1 is empty, median of [1, 2]
    assert find_median_sorted_arrays([], [1, 2]) == 1.5

def test_single_elements():
    # merged = [1, 2], median = 1.5
    assert find_median_sorted_arrays([1], [2]) == 1.5

def test_both_single_elements_same():
    # merged = [3, 3], median = 3.0
    assert find_median_sorted_arrays([3], [3]) == 3.0


# --- Interleaved values ---

def test_interleaved():
    # merged = [1, 2, 3, 4, 5, 6], median = (3+4)/2 = 3.5
    assert find_median_sorted_arrays([1, 3, 5], [2, 4, 6]) == 3.5

def test_all_in_first_array_smaller():
    # merged = [1, 2, 3, 4, 5], median = 3.0
    assert find_median_sorted_arrays([1, 2], [3, 4, 5]) == 3.0

def test_all_in_second_array_smaller():
    # merged = [1, 2, 3, 4, 5], median = 3.0
    assert find_median_sorted_arrays([3, 4, 5], [1, 2]) == 3.0


# --- Negative numbers ---

def test_negative_numbers():
    # merged = [-5, -3, -1, 0], median = (-3 + -1) / 2 = -2.0
    assert find_median_sorted_arrays([-5, -1], [-3, 0]) == -2.0

def test_mixed_negative_positive():
    # merged = [-1, 0, 1], median = 0.0
    assert find_median_sorted_arrays([-1, 1], [0]) == 0.0
