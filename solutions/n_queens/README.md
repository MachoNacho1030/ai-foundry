# N-Queens — LeetCode #51 (Hard)

---

## 1. Problem Summary

You have an `n x n` chessboard and `n` queens. Your job is to place all `n` queens on the board so that no queen can attack another.

In chess, a queen can attack anything in the same **row**, the same **column**, or along the same **diagonal** — in any direction, any number of squares away.

So the rules are:
- No two queens can share a row
- No two queens can share a column
- No two queens can sit on the same diagonal

Given a number `n`, return every possible valid arrangement. Each arrangement is represented as a list of strings — one string per row. A `Q` is a queen, a `.` is an empty square.

**Example:** For `n = 4`, there are exactly two valid arrangements:

```
. Q . .        . . Q .
. . . Q        Q . . .
Q . . .        . . . Q
. . Q .        . Q . .
```

**Constraints:** `1 <= n <= 9`

---

## 2. Approach

### What we considered

**Brute force** — generate every possible way to place `n` queens on the board and filter out the invalid ones. This works but is catastrophically slow — the number of combinations explodes as `n` grows. Ruled out immediately.

**Bitmask backtracking** — same idea as backtracking but uses binary integers and bitwise operations to track conflicts instead of sets. Faster in practice but much harder to read and explain. Overkill for this problem size (`n <= 9`).

**Backtracking (chosen)** — place queens one row at a time, top to bottom. For each row, try every column. Before placing, check if it's safe. If safe, place the queen and move to the next row. If you get stuck (no column is safe), go back to the previous row and try the next column there. This "try, fail, go back" process is called backtracking.

### Why backtracking

- It's the expected answer in a technical interview
- It's explainable out loud in plain English
- It prunes the search tree aggressively — most bad placements are caught early, so we never explore the full space
- Clean, readable code with no bit manipulation tricks

### Key insight

Because we place exactly one queen per row (top to bottom), we never need to check for row conflicts — they're impossible by construction. We only need to track column conflicts and diagonal conflicts, which we do with three sets.

---

## 3. How the Solution Works

The solution is a single function `solve_n_queens(n)` that uses an inner recursive function called `backtrack(row)`.

**Setup — three conflict trackers:**

Before we start, we create three sets:
- `cols` — tracks which columns are already occupied
- `diag1` — tracks occupied "top-left to bottom-right" diagonals. Every square on the same diagonal of this type has the same `row - col` value. For example, squares (0,1), (1,2), and (2,3) all have `row - col = -1`.
- `diag2` — tracks occupied "top-right to bottom-left" diagonals. Every square on the same diagonal of this type has the same `row + col` value. For example, squares (0,2), (1,1), and (2,0) all have `row + col = 2`.

We also keep `queen_cols` — a list that records which column we placed the queen in for each row as we go deeper.

**The recursive function `backtrack(row)`:**

- If `row == n`, we've successfully placed queens in all `n` rows. Convert `queen_cols` into a list of strings and add it to results.
- Otherwise, try every column `0` through `n-1` in the current row:
  - If the column is in `cols`, skip it — column conflict.
  - If `row - col` is in `diag1`, skip it — diagonal conflict.
  - If `row + col` is in `diag2`, skip it — diagonal conflict.
  - If none of the above, place the queen: add to all three sets, append to `queen_cols`, and recurse to `row + 1`.
  - After the recursive call returns, **undo** everything — remove from all three sets, pop from `queen_cols`. This is the backtrack step. It resets state so we can try the next column.

**Building the board string:**

When we have a complete solution, we build each row string like this: `"." * col + "Q" + "." * (n - col - 1)`. So if the queen is in column 2 on a 4-wide board, the row becomes `"..Q."`.

---

## 4. Test Coverage

All tests live in `ai-foundry/tests/test_n_queens.py`. Tests were written **before** the solution (TDD) and confirmed to fail (red) before the solution was written, then confirmed to pass (green) after.

| Test | What it checks | Why it matters |
|------|---------------|----------------|
| `test_n1_exact` | `n=1` returns `[["Q"]]` exactly | The trivial base case — one queen, one square |
| `test_n4_exact` | `n=4` returns both known solutions | Verifies exact output against the problem's given examples |
| `test_all_solutions_valid[1-9]` | Every solution for every `n` passes chess rules | Catches bugs that exact tests miss — ensures no queen attacks another |
| `test_solution_count[1-9]` | Each `n` returns exactly the right number of solutions | Catches duplicates and missing solutions |
| `test_n2_no_solutions` | `n=2` returns `[]` | No valid placement exists — we must return empty, not crash |
| `test_n3_no_solutions` | `n=3` returns `[]` | Same as above for `n=3` |
| `test_return_type_is_list_of_lists_of_strings` | Output shape is `List[List[str]]` | LeetCode format check — wrong types break submission |

**Result: 23/23 tests passing.**

---

## 5. Complexity

**Time: O(n!)**

In the worst case, the algorithm explores a tree of possibilities. The first row has `n` choices, the second has at most `n-1`, the third `n-2`, and so on. That's `n * (n-1) * (n-2) * ... * 1 = n!`. In practice it's much faster because we prune bad branches early — most columns are rejected before we recurse.

For `n=9`, the solution still runs in milliseconds because the pruning is aggressive.

**Space: O(n²)**

We store the board — `n` rows of `n` characters — for each complete solution. The three conflict sets use O(n) space each. The recursion stack goes `n` levels deep. Total: O(n²) dominated by board storage.

---

## 6. What Was Learned

The key insight in N-Queens is that diagonals can be uniquely identified by a single number — `row - col` for one direction and `row + col` for the other. This turns an expensive "scan the whole board" check into an O(1) set lookup. That trick shows up in other grid backtracking problems too.
