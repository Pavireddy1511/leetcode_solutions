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
        lH=self.dfsHeight(root.left)
        rH=self.dfsHeight(root.right)
        #balance factor stmt
        if lH == -1 or rH == -1:
            return -1

        if(abs(lH-rH)>1):
            return -1
        return 1+max(lH,rH)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfsHeight(root) != -1

        