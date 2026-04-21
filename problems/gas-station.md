# Gas Station — LeetCode #134

## Problem

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station
to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel
around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution,
it is guaranteed to be unique.

## Examples

### Example 1
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3

### Example 2
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1

## Constraints

- n == gas.length == cost.length
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4
- The input is generated such that the answer is unique.

## Approach

Greedy — O(n) time, O(1) space.

1. If total gas < total cost, return -1 (impossible regardless of start).
2. Otherwise, scan forward tracking a running tank balance.
3. When the tank goes negative, reset the candidate start to the next station and reset tank to 0.
4. The candidate start at the end of the pass is the answer.

Key insight: if you go negative at station k starting from station i, then i through k are all
invalid starts — you passed through them with surplus gas and still failed. Skip them all at once.
