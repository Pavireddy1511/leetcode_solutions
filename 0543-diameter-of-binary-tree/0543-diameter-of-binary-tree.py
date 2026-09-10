# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfsHeight(self,root:Optional[TreeNode]):
        if root is None:
            return 0
        ld=self.dfsHeight(root.left)
        rd=self.dfsHeight(root.right)
        #balance factor stmt
        self.maxDia = max(self.maxDia, ld+rd)
        return 1+max(ld, rd)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDia=0
        self.dfsHeight(root)
        return self.maxDia
        