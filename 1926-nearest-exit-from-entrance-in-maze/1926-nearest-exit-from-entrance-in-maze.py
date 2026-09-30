from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:

        n = len(maze)
        m = len(maze[0])

        dq = deque()

        # Add entrance
        dq.append((entrance[0], entrance[1], 0))

        # Mark entrance as visited
        maze[entrance[0]][entrance[1]] = '+'

        # Directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while dq:
            x, y, steps = dq.popleft()

            for d in directions:
                r = x + d[0]
                c = y + d[1]

                # Check inside maze and empty
                if (0 <= r < n and
                    0 <= c < m and
                    maze[r][c] == '.'):

                    # Check exit
                    if r == 0 or r == n - 1 or c == 0 or c == m - 1:
                        return steps + 1

                    # Mark visited
                    maze[r][c] = '+'

                    # Add to queue
                    dq.append((r, c, steps + 1))

        return -1
        