import pytest
from solutions.first_missing_positive import first_missing_positive


def test_missing_after_consecutive_start():
    assert first_missing_positive([1, 2, 0]) == 3


def test_missing_in_middle():
    assert first_missing_positive([3, 4, -1, 1]) == 2


def test_missing_one():
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1


def test_single_element_missing_one():
    assert first_missing_positive([2]) == 1


def test_single_element_is_one():
    assert first_missing_positive([1]) == 2


def test_all_negatives():
    assert first_missing_positive([-1, -2, -3]) == 1


def test_duplicates():
    assert first_missing_positive([1, 1, 2, 2]) == 3


def test_full_consecutive_range():
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6
