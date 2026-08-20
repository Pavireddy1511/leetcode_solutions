class Solution:

    count = 0

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
        while i >=0 and j >=0:
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
            return 1

        count = 0

        # placing the queens on the board
        for col in range(n):
            if self.isSafe(row, col, cboard, n):
                cboard[row][col] = 'Q'

                count += self.backTracking(
                    row + 1, n, cboard, res
                )

                cboard[row][col] = '.'

        return count

    def totalNQueens(self, n: int):

        cboard = [['.'] * n for _ in range(n)]

        count = self.backTracking(0, n, cboard, [])

        return count