import pytest
from solutions.largest_number import largest_number


# =============================================================================
# HOW THIS PROBLEM WORKS (read this first)
# =============================================================================
# The goal: given a list of numbers, arrange them so that when you smash them
# together as a string, you get the biggest possible number.
#
# The key insight: to decide if number A should come before number B,
# compare the string "AB" vs "BA". Whichever is bigger wins.
#
# Example: A=9, B=34
#   "934" vs "349"  →  "934" is bigger  →  9 goes first
#
# Example: A=30, B=3
#   "303" vs "330"  →  "330" is bigger  →  3 goes first
#
# We sort ALL numbers using this comparison, then join them into one string.
# =============================================================================


# --- Examples from problem statement ---

def test_example_one():
    # Input:  [10, 2]
    # Compare "210" vs "102" → "210" wins → 2 goes before 10
    # Output: "210"
    assert largest_number([10, 2]) == "210"

def test_example_two():
    # Input:  [3, 30, 34, 5, 9]
    # Sorted by our comparator: 9, 5, 34, 3, 30
    #   9 vs 5  → "95" > "59"  → 9 first
    #   5 vs 34 → "534" > "345" → 5 next
    #   34 vs 3 → "343" > "334" → 34 next
    #   3 vs 30 → "330" > "303" → 3 before 30
    # Joined: "9534330"
    assert largest_number([3, 30, 34, 5, 9]) == "9534330"


# --- Single element ---

def test_single_element():
    # Only one number in the list — no sorting needed.
    # The result is just that number as a string.
    # Input: [5] → Output: "5"
    assert largest_number([5]) == "5"

def test_single_zero():
    # Edge case: a list with just [0].
    # Should return "0", not an empty string or crash.
    assert largest_number([0]) == "0"


# --- All zeros edge case ---

def test_all_zeros():
    # If every number is 0, joining them naively gives "000".
    # But the correct answer is just "0" — there's no such number as "000".
    # The solution must detect this and return "0" instead.
    # Input: [0, 0, 0] → Output: "0"
    assert largest_number([0, 0, 0]) == "0"


# --- Two numbers, order matters ---

def test_two_numbers_swap_needed():
    # Input: [21, 3]
    # Compare "321" vs "213" → "321" > "213" → 3 goes before 21
    # Output: "321"
    assert largest_number([21, 3]) == "321"

def test_two_numbers_no_swap():
    # Input: [5, 6]
    # Compare "65" vs "56" → "65" > "56" → 6 goes before 5
    # Output: "65"
    assert largest_number([5, 6]) == "65"


# --- Numbers with shared prefix (tricky case) ---

def test_shared_prefix():
    # Input: [3, 30, 34]
    # These all start with "3" — easy to get confused.
    # 34 vs 30: "3430" > "3034" → 34 before 30
    # 34 vs 3:  "343"  > "334"  → 34 before 3
    # 3  vs 30: "330"  > "303"  → 3 before 30
    # Final order: 34, 3, 30 → "34330"
    assert largest_number([3, 30, 34]) == "34330"


# --- Large values ---

def test_large_values():
    # Input: [999999999, 1]
    # Compare "9999999991" vs "1999999999"
    # "9999999991" is clearly bigger → 999999999 goes first
    # Output: "9999999991"
    assert largest_number([999999999, 1]) == "9999999991"
