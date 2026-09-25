class Solution:
    def dfs(self, grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) :
            return False
        if grid[i][j]==1:
            return True    
        grid[i][j]=1
        
        up = self.dfs(grid, i - 1, j)
        down = self.dfs(grid, i + 1, j)
        left = self.dfs(grid, i, j - 1)
        right = self.dfs(grid, i, j + 1)

        return up and down and left and right
    

    def closedIsland(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        closedIsl=0
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]==0:
                    if self.dfs(grid,i,j):
                         closedIsl+=1
        return closedIsl

        