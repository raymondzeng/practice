class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        result = []
        stack = []
        
        while (len(stack) != 0 or not root is None):
            if root is None:
                root = stack.pop()
                result.append(root.val)
                root = None
            else:
                stack.append(root)
                
                if not root.left is None:
                    stack.append(root.left)
                
                root = root.right
            
        return result

s = Solution()
print s.postorderTraversal(TreeNode(1))
