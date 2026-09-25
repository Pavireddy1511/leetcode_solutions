class Solution:
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 0 
        if grid[i][j] == 0:
            return

        grid[i][j] = 0
     
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)
    def numEnclaves(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        count=0
        for i in range(n):
            if grid[i][0] == 1:
                self.dfs(grid, i, 0)
            if grid[i][m-1] == 1:
                self.dfs(grid, i, m-1)
        for j in range(m):
            if grid[0][j] == 1:
                self.dfs(grid, 0, j)
            if grid[n-1][j] == 1:
                self.dfs(grid, n-1, j)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        return count            

         
        

        