# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
            
        return self.maxDepth(root, 1) <= 1

    def maxDepth(self, root, depth):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        if root.left is not None and root.right is None:
            return 1
        if root.left is None and root.right is not None:
            return 1
            
        diff = max(self.maxDepth(root.left, depth), self.maxDepth(root.right, depth))
        
        return depth + diff


s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)
t.left.left = TreeNode(3)
t.left.left.left = TreeNode(4)
t.right.right = TreeNode(3)
t.right.right.right = TreeNode(4)


print s.isBalanced(t)
