import pytest
from solutions.best_time_to_buy_sell_stock_iii import max_profit


# --- LeetCode provided examples ---

def test_example_one():
    # prices = [3,3,5,0,0,3,1,4]
    # Best strategy: buy on day 4 (price=0), sell on day 6 (price=3) → profit +3
    #                buy on day 7 (price=1), sell on day 8 (price=4) → profit +3
    # Total: 6. Two separate dip-and-rise windows, both captured.
    assert max_profit([3, 3, 5, 0, 0, 3, 1, 4]) == 6

def test_example_two():
    # prices = [1,2,3,4,5] — steadily rising the whole time
    # Best strategy: one transaction — buy on day 1 (price=1), sell on day 5 (price=5)
    # Using both transactions can't help because there's no second dip to buy into
    # Total: 4
    assert max_profit([1, 2, 3, 4, 5]) == 4

def test_example_three():
    # prices = [7,6,4,3,1] — steadily falling the whole time
    # Every sell price is lower than every buy price — no profitable trade exists
    # Total: 0 (we never transact)
    assert max_profit([7, 6, 4, 3, 1]) == 0


# --- Edge cases ---

def test_single_element():
    # Only one day means you can buy but never sell — no transaction possible
    # Expected: 0
    assert max_profit([5]) == 0

def test_two_elements_profit():
    # Buy on day 1 (price=1), sell on day 2 (price=5) → profit +4
    # Minimum viable profitable input
    assert max_profit([1, 5]) == 4

def test_two_elements_no_profit():
    # Price falls from 5 to 1 — selling would lose money so we skip the trade
    # Expected: 0
    assert max_profit([5, 1]) == 0

def test_all_same_price():
    # Every price is identical — buying and selling at the same price gives 0 profit
    # No point in transacting at all
    assert max_profit([3, 3, 3, 3]) == 0


# --- Two transactions better than one ---

def test_two_transactions_beat_one():
    # prices = [1, 6, 1, 6]
    # One transaction: buy@1, sell@6 → profit 5
    # Two transactions: buy@1, sell@6, buy@1, sell@6 → profit 10
    # This test confirms we're correctly using both allowed transactions
    assert max_profit([1, 6, 1, 6]) == 10


# --- Large input (performance) ---

def test_large_input_performance():
    # 100,000 prices alternating between 0 and 100
    # Pattern: [0, 100, 0, 100, ...]
    # We can only do 2 transactions max, so best we can do:
    #   buy at first 0 (day 1), sell at 100 (day 2) → +100
    #   buy at next 0 (day 3), sell at 100 (day 4) → +100
    # Total: 200
    # This also verifies O(n) performance — should complete instantly
    prices = [0, 100] * 50_000
    result = max_profit(prices)
    assert result == 200
