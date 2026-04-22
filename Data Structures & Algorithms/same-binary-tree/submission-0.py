# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, arr):
            if not node:
                arr.append(None)   # marker for structure
                return
            arr.append(node.val)
            dfs(node.left, arr)
            dfs(node.right, arr)
        
        arr1, arr2 = [], []
        dfs(p, arr1)
        dfs(q, arr2)

        return arr1 == arr2
