# Problem: Median of Two Sorted Arrays

**LeetCode #4 — Hard**

## Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall run time complexity should be `O(log(min(m, n)))`.

## Examples

**Example 1:**
- Input: nums1 = [1, 3], nums2 = [2]
- Output: 2.0
- Explanation: merged = [1, 2, 3], median = 2.0

**Example 2:**
- Input: nums1 = [1, 2], nums2 = [3, 4]
- Output: 2.5
- Explanation: merged = [1, 2, 3, 4], median = (2 + 3) / 2 = 2.5

## Constraints

- 0 <= m, n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
