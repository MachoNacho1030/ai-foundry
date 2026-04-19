# Problem: Two Sum

## Source
LeetCode #1 — Easy
https://leetcode.com/problems/two-sum/

## Problem Statement
Given an array of integers nums and an integer target,
return the indices of the two numbers that add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

## Examples

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

## Constraints
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists

## Approach
1. Naive approach — nested loops O(n^2) time complexity
2. Optimized approach — hashmap O(n) time complexity

## Why Hashmap
Instead of checking every pair of numbers,
we store each number we have seen in a hashmap.
For each new number we check if its complement already exists.
This reduces time complexity from O(n^2) to O(n).

## Test Cases To Cover
- Standard case — two numbers add up to target
- Middle elements — target pair not at start
- Duplicate numbers — array contains duplicates
- Negative numbers — array contains negatives
- Edge case — empty array
- Large input — performance test

## Branch
feature/two-sum

## Status
In Progress