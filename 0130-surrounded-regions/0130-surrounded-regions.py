class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        n = len(board)
        m = len(board[0])

        # Check the first and last columns
        for i in range(n):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            if board[i][m - 1] == 'O':
                self.dfs(board, i, m - 1)

        # Check the first and last rows
        for j in range(m):
            if board[0][j] == 'O':
                self.dfs(board, 0, j)
            if board[n - 1][j] == 'O':
                self.dfs(board, n - 1, j)

        # Capture surrounded regions
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        if (i < 0 or j < 0 or
                i >= len(board) or j >= len(board[0])):
            return

        if board[i][j] != 'O':
            return

        # Mark boundary-connected O cells as safe
        board[i][j] = '#'

        self.dfs(board, i - 1, j)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)
     
        