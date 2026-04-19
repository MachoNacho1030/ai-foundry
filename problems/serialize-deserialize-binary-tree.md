# Problem: Serialize and Deserialize Binary Tree

**Source:** LeetCode 297 — Hard

## Problem Statement

Design an algorithm to serialize and deserialize a binary tree.

- **Serialize:** Convert a binary tree into a string
- **Deserialize:** Convert that string back into the original binary tree

There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and this string
can be deserialized to the original tree structure.

## Example

Input tree:
```
    1
   / \
  2   3
     / \
    4   5
```

Serialized: `"1,2,3,null,null,4,5"`
Deserialized: same tree as above

## Constraints
- The number of nodes in the tree is in the range [0, 10^4]
- Node values are in the range [-1000, 1000]

## Approach
Use BFS (level-order traversal) to serialize.
Use a queue to reconstruct during deserialization.
Mark missing children as "null" so gaps are preserved.
