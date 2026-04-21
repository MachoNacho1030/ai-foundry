# Problem: Single Number

## Source
LeetCode #136 — Easy
https://leetcode.com/problems/single-number/

## Problem Statement
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

## Examples

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

## Constraints
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
- Each element appears twice except for exactly one element which appears only once

## Approach
- XOR (bitwise exclusive or) — O(n) time, O(1) space

## Why XOR
XOR has two key properties:
- Any number XOR itself equals 0 (n ^ n = 0)
- Any number XOR 0 equals itself (n ^ 0 = n)

XOR every element together. All pairs cancel out to 0.
The lone element has nothing to cancel with — it survives as the result.

## Test Cases To Cover
- Standard case — single element at the end
- Single element at the start
- Single element in the middle
- Single-element array
- Negative numbers — array contains negatives
- Large input — performance test

## Branch
feature/single-number

## Status
In Progress
