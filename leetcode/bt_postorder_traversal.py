class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive
    #  if root is None:
    #      return []
        
    #  return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    
    # DOEDSN"T WORK 
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        result = []
        stack = []
        
        while (len(stack) != 0 or root is not None):
            if root is None:
                root = stack.pop()
                result.append(root.val)
                root = None
            else:
                stack.append(root)
                
                if root.right is not None:
                    stack.append(root.right)
                
                root = root.left
            
        return result

s = Solution()
t = TreeNode(2)
t.left = TreeNode(3)
t.left.left = TreeNode(1)
print s.postorderTraversal(t)
