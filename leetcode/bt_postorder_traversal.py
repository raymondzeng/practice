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
        
        while(True):
            while(root):    
                stack.append(root)
                root = root.left
            
            while(len(stack) > 0 and root == stack[-1].right):
                root = stack.pop()
                result.append(root.val)
            if len(stack) == 0: break

            root = stack[-1].right
            
        return result

s = Solution()
t = TreeNode(1)
t.right = TreeNode(2)
print s.postorderTraversal(t)
