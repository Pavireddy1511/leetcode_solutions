# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        ln = self.isSameTree(p.left,q.right)
        rn=self.isSameTree(p.right,q.left)
        return ln and rn    

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left,root.right)
        