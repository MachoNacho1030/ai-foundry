import pytest
from solutions.n_queens.n_queens import solve_n_queens


# ─── Helper: validate a single board solution ────────────────────────────────

def is_valid_solution(board):
    """
    The referee function. Given one solution (a list of strings like [".Q..", "...Q", ...]),
    this checks all three chess rules that make a queen placement valid:
      1. Each row has exactly one queen
      2. No two queens share the same column
      3. No two queens sit on the same diagonal (top-left or top-right)
    Returns True if valid, raises AssertionError if not.
    """
    n = len(board)

    # Step 1: Find which column the queen sits in for each row.
    # We collect these into a list so we can compare pairs later.
    queen_cols = []
    for row in board:
        # Count how many 'Q' characters are in this row — must be exactly 1
        q_count = row.count('Q')
        assert q_count == 1, f"Row '{row}' has {q_count} queens, expected 1"
        # Record the column index of the queen in this row
        queen_cols.append(row.index('Q'))

    # Step 2: Compare every pair of rows to check for column and diagonal conflicts.
    # We use i and j as row indices — i is always earlier than j.
    for i in range(n):
        for j in range(i + 1, n):
            # Column conflict: two queens in the same column means same col index
            assert queen_cols[i] != queen_cols[j], (
                f"Column conflict: rows {i} and {j} both in col {queen_cols[i]}"
            )
            # Diagonal conflict: queens are on the same diagonal if the difference
            # in their columns equals the difference in their rows.
            # e.g. row 0 col 1, row 2 col 3 → |1-3| == |0-2| → diagonal attack
            assert abs(queen_cols[i] - queen_cols[j]) != abs(i - j), (
                f"Diagonal conflict: rows {i} and {j}"
            )

    return True


# ─── Known solution counts per n ─────────────────────────────────────────────

# These are the mathematically proven counts of distinct N-Queens solutions.
# n=2 and n=3 have zero solutions — on those small boards, any queen placement
# will always leave at least two queens attacking each other. No way around it.
KNOWN_COUNTS = {
    1: 1,    # trivial — one queen, one square
    2: 0,    # impossible — queens always conflict
    3: 0,    # impossible — queens always conflict
    4: 2,    # two valid arrangements (the ones shown in the problem)
    5: 10,   # ten valid arrangements
    6: 4,    # four valid arrangements
    7: 40,   # forty valid arrangements
    8: 92,   # ninety-two (the classic "8 queens" problem)
    9: 352,  # three hundred and fifty-two valid arrangements
}


# ─── Exact output tests ───────────────────────────────────────────────────────

def test_n1_exact():
    # The simplest case: a 1x1 board with one queen.
    # There is only one possible placement — the single square.
    # We assert the output matches exactly.
    result = solve_n_queens(1)
    assert result == [["Q"]]


def test_n4_exact():
    # n=4 is the smallest interesting case — it has exactly two solutions.
    # We define both expected solutions here (taken from the LeetCode problem statement).
    # We sort both lists before comparing so that order differences don't cause false failures —
    # the problem says "you may return the answer in any order."
    result = solve_n_queens(4)
    expected = [
        [".Q..", "...Q", "Q...", "..Q."],  # first valid arrangement
        ["..Q.", "Q...", "...Q", ".Q.."],  # second valid arrangement
    ]
    assert sorted(result) == sorted(expected)


# ─── Property tests: every solution must be a valid chess placement ───────────

@pytest.mark.parametrize("n", range(1, 10))
def test_all_solutions_valid(n):
    # For every board size from 1 to 9, every solution we return must pass
    # the chess rules check. This catches bugs that exact output tests might miss —
    # for example, if we return a "solution" where queens attack each other.
    result = solve_n_queens(n)
    for solution in result:
        # The board must have exactly n rows
        assert len(solution) == n, f"Board should have {n} rows, got {len(solution)}"
        # Every row must have exactly n characters (the board is n x n)
        assert all(len(row) == n for row in solution), f"Each row should have {n} cols"
        # Run the full chess rules check on this solution
        is_valid_solution(solution)


# ─── Solution count tests ─────────────────────────────────────────────────────

@pytest.mark.parametrize("n,expected_count", KNOWN_COUNTS.items())
def test_solution_count(n, expected_count):
    # For each board size, check that we return exactly the right number of solutions.
    # This catches two failure modes:
    #   - Too few: we're pruning valid solutions by mistake
    #   - Too many: we're returning duplicates or invalid arrangements
    result = solve_n_queens(n)
    assert len(result) == expected_count, (
        f"n={n}: expected {expected_count} solutions, got {len(result)}"
    )


# ─── Edge cases ───────────────────────────────────────────────────────────────

def test_n2_no_solutions():
    # On a 2x2 board, there is no valid placement for 2 queens.
    # Any two queens placed will always share a row, column, or diagonal.
    # We must return an empty list — not None, not an error, just [].
    assert solve_n_queens(2) == []


def test_n3_no_solutions():
    # Same situation for a 3x3 board — no valid placement exists.
    # Again, we expect an empty list.
    assert solve_n_queens(3) == []


def test_return_type_is_list_of_lists_of_strings():
    # LeetCode expects a specific output shape: List[List[str]].
    # This test verifies the types at every level of nesting:
    #   - The outer container is a list
    #   - Each solution inside is a list
    #   - Each row inside a solution is a string
    result = solve_n_queens(4)
    assert isinstance(result, list), "Outer result must be a list"
    for solution in result:
        assert isinstance(solution, list), "Each solution must be a list"
        for row in solution:
            assert isinstance(row, str), "Each row must be a string"
