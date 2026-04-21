import pytest
from solutions.gas_station import can_complete_circuit


# --- Example cases from the problem statement ---

def test_example_one():
    # Standard case: starting at index 3 is the only valid start
    # Net gains: [-2, -2, -2, +3, +3] — only station 3 starts a non-negative streak
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    assert can_complete_circuit(gas, cost) == 3

def test_example_two():
    # Impossible case: total gas (9) < total cost (10), no start works
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    assert can_complete_circuit(gas, cost) == -1


# --- Edge cases ---

def test_single_station_can_complete():
    # Only one station — fill up and immediately "arrive back", no travel needed
    # gas >= cost means we have enough to stay in place
    gas = [5]
    cost = [3]
    assert can_complete_circuit(gas, cost) == 0

def test_single_station_cannot_complete():
    # Only one station but gas < cost — can't even leave
    gas = [1]
    cost = [2]
    assert can_complete_circuit(gas, cost) == -1

def test_all_zeros():
    # Every station gives zero gas and costs zero — technically completable from index 0
    gas = [0, 0, 0]
    cost = [0, 0, 0]
    assert can_complete_circuit(gas, cost) == 0

def test_answer_at_index_zero():
    # Valid start is the very first station — make sure we don't skip it
    gas = [5, 1, 1]
    cost = [1, 4, 2]
    assert can_complete_circuit(gas, cost) == 0

def test_answer_at_last_index():
    # Valid start is the last station — tests that the greedy resets all the way to the end
    gas = [1, 1, 5]
    cost = [2, 3, 1]
    assert can_complete_circuit(gas, cost) == 2

def test_total_gas_less_than_total_cost():
    # Total gas is strictly less than total cost — impossible regardless of start
    # sum(gas) = 3, sum(cost) = 10
    gas = [1, 1, 1]
    cost = [4, 3, 3]
    assert can_complete_circuit(gas, cost) == -1
