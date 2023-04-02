# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def height(node):
            if not node:
                return 0
            
            l_subtree_height = height(node.left)
            r_subtree_height = height(node.right)

            return 1 + max(l_subtree_height, r_subtree_height)
        
        l_subtree_height = height(root.left)
        r_subtree_height = height(root.right)
        if abs(l_subtree_height - r_subtree_height) > 1:
            return False
        

        return self.isBalanced(root.left) and self.isBalanced(root.right)

