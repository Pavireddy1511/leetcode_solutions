class Solution:
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0 :
            return 1
        if grid[i][j]==2:
            return 0 
        grid[i][j] = 2      
        return (self.dfs(grid,i-1,j)+
        self.dfs(grid,i+1,j)+
        self.dfs(grid,i,j-1)+
        self.dfs(grid,i,j+1))   

    def islandPerimeter(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        perim=0
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]==1:
                    perim +=self.dfs(grid,i,j)
        return perim            
        