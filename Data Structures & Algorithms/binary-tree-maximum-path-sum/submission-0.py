# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        # we want to return the max without split here:
        def dfs(root):
            if not root:
                return 0
            else: 
                leftMax = dfs(root.left)
                rightMax = dfs(root.right)
                leftMax = max(leftMax, 0)
                rightMax = max(rightMax, 0)

                res[0] = max(res[0], root.val + leftMax + rightMax)
                return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]