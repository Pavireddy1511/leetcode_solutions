# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque()
        if root is None:
            return res
        q.append(root)
    

        while q:
            n=len(q)
            for i in range(n):
                temp=q.popleft()
                if i==n-1:
                    res.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            
        return res  