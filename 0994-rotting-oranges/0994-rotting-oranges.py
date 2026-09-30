from collections import deque

class Solution:
    def orangesRotting(self, grid):
        n = len(grid)
        m = len(grid[0])

        minutes = -1

        # BFS => deque
        dq = deque()
        fresh = 0

        # Find all rotten and fresh oranges
        for r in range(n):
            for c in range(m):

                # Rotten orange
                if grid[r][c] == 2:
                    dq.append((r, c))

                # Fresh orange
                elif grid[r][c] == 1:
                    fresh += 1

        # If all oranges are already rotten
        if fresh == 0:
            return 0

        # Direction array
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        # Process the deque
        while dq:
            size = len(dq)

            for i in range(size):
                x, y = dq.popleft()

                # For-each loop
                for d in directions:
                    r = x + d[0]
                    c = y + d[1]

                    # Inside the grid and fresh orange
                    if (r >= 0 and c >= 0 and
                        r < n and c < m and
                        grid[r][c] == 1):

                        grid[r][c] = 2
                        fresh -= 1
                        dq.append((r, c))

            minutes += 1

        return minutes if fresh == 0 else -1
                

