class Solution:
    def dfs(self,image,sr,sc,color,startColor):
        n=len(image)
        m=len(image[0])
        if sr<0 or sc<0 or sr>=n or sc>=m or image[sr][sc]==color:
            return
        existingColor=image[sr][sc]
        if startColor==existingColor:
            image[sr][sc]=color
        else:
            return    
        self.dfs(image,sr,sc-1,color,startColor)
        self.dfs(image,sr-1,sc,color,startColor)
        self.dfs(image,sr,sc+1,color,startColor)
        self.dfs(image,sr+1,sc,color,startColor)    

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        newColor=image[sr][sc]
        if newColor == color:
            return image

        self.dfs(image,sr,sc,color,newColor)
        return image