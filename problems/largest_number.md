# Largest Number

**Difficulty:** Medium
**Source:** LeetCode 179

## Problem

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it as a string.

## Examples

**Example 1:**
```
Input:  nums = [10, 2]
Output: "210"
```

**Example 2:**
```
Input:  nums = [3, 30, 34, 5, 9]
Output: "9534330"
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 10^9`

## Approach

Sort numbers using a custom comparator: for two numbers `a` and `b`, compare the concatenations `str(a) + str(b)` vs `str(b) + str(a)`. Whichever is larger determines the order. Join the sorted result into a single string.

**Edge case:** if the largest number is `0` (all zeros), return `"0"`.
