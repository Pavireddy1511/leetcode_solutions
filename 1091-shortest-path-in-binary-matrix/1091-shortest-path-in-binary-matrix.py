from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:

        n = len(grid)

        # Check top-left and bottom-right
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        q = deque()

        # row, column, path
        q.append((0, 0, 1))

        # Mark visited
        grid[0][0] = 1

        # 8 directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        # BFS
        while q:

            x, y, path = q.popleft()

            # Reached bottom-right
            if x == n - 1 and y == n - 1:
                return path

            # Check 8 directions
            for d in directions:

                r = x + d[0]
                c = y + d[1]

                # Check inside grid and cell is 0
                if (r >= 0 and r < n and
                    c >= 0 and c < n and
                    grid[r][c] == 0):

                    q.append((r, c, path + 1))

                    # Mark visited
                    grid[r][c] = 1

        return -1   

        


        