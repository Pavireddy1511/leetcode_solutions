# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=deque()
        if root is None:
            return res
        q.append(root)
        flag=True
        while q:
            level=[]
            for i in range(len(q)):
                temp=q.popleft()
                if flag:
                    level.append(temp.val)
                else:
                    level.insert(0,temp.val)    
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            res.insert(0,level) 
           
        return res  
        