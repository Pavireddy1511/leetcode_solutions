class Solution:

    def isSafe(self, row, col, cboard, n):

        # horizontal check
        for i in range(n):
            if cboard[row][i] == 'Q':
                return False

        # vertical check
        for j in range(n):
            if cboard[j][col] == 'Q':
                return False

        # left diagonal check
        i, j = row, col
        while i >=0 and j >= 0:
            if cboard[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # right diagonal check
        i, j = row, col
        while i >= 0 and j < n:
            if cboard[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backTracking(self, row, n, cboard, res):

        if row == n:
            x = []
            for i in range(n):
                x.append(''.join(cboard[i]))
            res.append(x)
            return

        # placing the queens on the board
        for col in range(n):
            if self.isSafe(row, col, cboard, n):
                cboard[row][col] = 'Q'
                self.backTracking(row + 1, n, cboard, res)
                cboard[row][col] = '.'

    def solveNQueens(self, n: int):

        res = []

        # [["..Q."]]
        cboard = [['.'] * n for _ in range(n)]

        self.backTracking(0, n, cboard, res)

        return res

        