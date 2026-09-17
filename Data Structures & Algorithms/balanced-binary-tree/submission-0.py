# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Check if any subtrees are inbalanced (return -1 if imbalanced)
        def dfs(node):
            if not node: #empty tree is a valid tree
                return 0
            lh = dfs(node.left) #find height of left subtree
            if lh == -1:
                return -1
            rh = dfs(node.right) #find height of right subtree
            if rh == -1:
                return -1
            if abs(lh - rh) > 1: #check if height diff > 1
                return -1
            return 1 + max(lh, rh) #return the taller  balanced subtree hight + root, 
        
        return dfs(root) != -1 #if -1 is returned, the tree is not balanced