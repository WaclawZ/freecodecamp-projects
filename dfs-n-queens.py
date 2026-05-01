def dfs_n_queens(n: int) -> list:
    if n < 1:
        return []

    solutions = []

    def is_safe(current_board, current_row, col):
        for r in range(current_row):
            c = current_board[r]

            if c == col:
                return False

            if abs(c - col) == abs(r - current_row):
                return False

        return True

    def dfs(row, current_board):
        if row == n:
            solutions.append(current_board[:])
            return

        for col in range(n):
            if is_safe(current_board, row, col):
                current_board.append(col)

                dfs(row + 1, current_board)

                current_board.pop()

    dfs(0, [])

    return solutions
