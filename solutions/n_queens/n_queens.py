def solve_n_queens(n: int) -> list[list[str]]:
    """
    Given an integer n, return all distinct solutions to the n-queens puzzle.
    Each solution is a list of n strings, where 'Q' is a queen and '.' is empty.

    Approach: backtracking — place one queen per row, top to bottom.
    At each row, try every column. If safe, place it and recurse to the next row.
    If no column works, backtrack to the previous row and try the next column there.
    """

    # This will hold all valid complete board configurations we find.
    # Each entry is a list of n strings (one per row).
    results = []

    # cols tracks which columns are already occupied by a queen.
    # If a queen is in column 2, no future queen can go in column 2.
    cols = set()

    # diag1 tracks the "top-left to bottom-right" diagonals.
    # Every square on the same diagonal of this type shares the same (row - col) value.
    # e.g. (0,1), (1,2), (2,3) all have row - col = -1 — same diagonal.
    diag1 = set()

    # diag2 tracks the "top-right to bottom-left" diagonals.
    # Every square on the same diagonal of this type shares the same (row + col) value.
    # e.g. (0,2), (1,1), (2,0) all have row + col = 2 — same diagonal.
    diag2 = set()

    # queen_cols is our working record of where we've placed queens so far.
    # queen_cols[r] = c means "in row r, we placed a queen in column c".
    # We build this up as we go deeper into the recursion.
    queen_cols = []

    def backtrack(row: int):
        """
        Try to place a queen in the given row.
        If row == n, we've successfully placed all n queens — record the solution.
        Otherwise, try every column in this row and recurse if the placement is safe.
        """

        # Base case: we've filled all n rows successfully.
        # Convert our column record into the required list-of-strings format and save it.
        if row == n:
            # Build one string per row.
            # For each row r, the queen is at queen_cols[r].
            # A row of width n with a queen at column c looks like:
            #   c dots, then 'Q', then (n - c - 1) dots.
            board = [
                "." * c + "Q" + "." * (n - c - 1)  # construct the row string
                for c in queen_cols                  # one string per queen placement
            ]
            # Append this complete board to our results list.
            results.append(board)
            # Stop recursing — this branch is done.
            return

        # Try placing a queen in every column of the current row.
        for col in range(n):

            # Check if this column is already used by a queen in a previous row.
            # If so, placing here would create a column conflict — skip it.
            if col in cols:
                continue

            # Check if this square is on an already-used top-left-to-bottom-right diagonal.
            # Two squares share this diagonal if they have the same (row - col) value.
            if (row - col) in diag1:
                continue

            # Check if this square is on an already-used top-right-to-bottom-left diagonal.
            # Two squares share this diagonal if they have the same (row + col) value.
            if (row + col) in diag2:
                continue

            # This column is safe. Place the queen here.
            # Record the column, and mark this column + both diagonals as occupied.
            cols.add(col)           # mark column as used
            diag1.add(row - col)    # mark this top-left diagonal as used
            diag2.add(row + col)    # mark this top-right diagonal as used
            queen_cols.append(col)  # record which column we chose for this row

            # Recurse: move to the next row and try to place the next queen.
            backtrack(row + 1)

            # Backtrack: undo the placement so we can try the next column.
            # We remove the queen and clear the column + diagonal markers.
            cols.remove(col)           # free up this column
            diag1.remove(row - col)    # free up this top-left diagonal
            diag2.remove(row + col)    # free up this top-right diagonal
            queen_cols.pop()           # remove the last recorded queen position

    # Kick off the recursion starting from row 0 (the top of the board).
    backtrack(0)

    # Return all valid board configurations we collected.
    return results
