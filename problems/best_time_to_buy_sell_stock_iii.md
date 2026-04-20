# 123. Best Time to Buy and Sell Stock III (Hard)

## Problem
Given an array `prices` where `prices[i]` is the price of a stock on day `i`, find the maximum profit using **at most two transactions**.

You must sell before you buy again.

## Examples

**Example 1:**
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy day 4 (0), sell day 6 (3) → +3. Buy day 7 (1), sell day 8 (4) → +3.

**Example 2:**
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy day 1 (1), sell day 5 (5) → +4.

**Example 3:**
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profitable transaction possible.

## Constraints
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^5

## Approach
State machine with 4 variables (O(n) time, O(1) space):
- hold1: best outcome after buying once
- sold1: best outcome after selling once
- hold2: best outcome after buying a second time
- sold2: best outcome after selling twice (answer)
