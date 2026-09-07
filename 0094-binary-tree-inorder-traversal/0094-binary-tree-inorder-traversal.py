# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        # recursion condition
        if root is None:
            return res
        # root left right 
        # logic 
        # go left by recursion
        res+=self.inorderTraversal(root.left)
        
        res.append(root.val)
        # go right ny recursion
        res+=self.inorderTraversal(root.right)
        return res
        