# N-Queens

**LeetCode #51 — Hard**

## Problem

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

## Examples

**Example 1:**
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
```

**Example 2:**
```
Input: n = 1
Output: [["Q"]]
```

## Constraints

- 1 <= n <= 9

## Approach

Backtracking — place queens row by row, trying each column. If a placement is safe (no conflict on column or diagonal), recurse to the next row. If stuck, backtrack and try the next column.

## Complexity

- Time: O(n!) — pruned search tree
- Space: O(n²) — board storage
