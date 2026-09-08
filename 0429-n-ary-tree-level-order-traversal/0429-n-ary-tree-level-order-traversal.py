"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        q=deque()
        if root is None:
            return res
        q.append(root)
        while q:
            level=[]
        
            for i in range(len(q)):
                temp=q.popleft()
                level.append(temp.val)
                for child in temp.children:
                    q.append(child)

                #if temp.left:
                   # q.append(temp.left)
                #if temp.right:
                    #q.append(temp.right)
            res.append(level)
        return res 
        