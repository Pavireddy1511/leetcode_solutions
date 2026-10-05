# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        result = []

        def dfs(node, target, path):

            if node is None:
                return

            path.append(node.val)

            if node.left is None and node.right is None:
                if node.val == target:
                    result.append(path.copy())

            dfs(node.left, target - node.val, path)
            dfs(node.right, target - node.val, path)

            path.pop()

        dfs(root, targetSum, [])

        return result
        