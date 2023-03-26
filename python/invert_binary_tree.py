# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #set base case for if root == None to end recursive calls
        if root == None: return None
        
        #create a temporary holder for either the left or right of the root (gonna go with root.right) so we can keep track of a value
        tmp = root.right
        #if temporary variable is set to root.right swap value of root.right to root.left (reversing them)
        root.right = root.left
        #set root.left to temporary variable
        root.left = tmp

        #recursively call function on the left to reverse each branch
        self.invertTree(root.left)
        #recursively call function on the right to reverse each branch of the right
        self.invertTree(root.right)
        
        #return root
        return root