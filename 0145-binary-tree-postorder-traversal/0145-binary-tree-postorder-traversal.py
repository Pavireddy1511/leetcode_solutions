# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        # recursion condition
        if root is None:
            return res
        # root left right 
        # logic 
        
        # go left by recursion
        res+=self.postorderTraversal(root.left)
        # go right ny recursion
        res+=self.postorderTraversal(root.right)
        res.append(root.val)
        return res
        