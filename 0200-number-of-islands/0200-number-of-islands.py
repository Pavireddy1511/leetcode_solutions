class Solution:
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0':
            return
        grid[i][j]='0'
        self.dfs(grid,i-1,j)
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j-1)
        self.dfs(grid,i,j+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        count=0
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]=='1':
                    count+=1
                    self.dfs(grid,i,j)
        return count            

        