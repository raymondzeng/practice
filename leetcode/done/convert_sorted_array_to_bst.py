# Given an array where elements are sorted in ascending order, 
# convert it to a height balanced BST.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0:
            return None
            
        split_at = len(num) // 2
        root = num[split_at]
        left = num[:split_at]
        right = num[split_at + 1:]
        
        node = TreeNode(root)
        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)
        return node

s = Solution()
t = TreeNode(1)
t.right = TreeNode(2)
print s.postorderTraversal(t)
