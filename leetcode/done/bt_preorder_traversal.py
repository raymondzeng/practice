class Solution:
    # @param root, a tree node
    # @return a list of integers
    
    # recursive solution
    # def preorderTraversal(self, root):
    #    if root is None:
    #        return []
    #    left_traverse = [] if root.left is None else self.preorderTraversal(root.left)
    #    right_traverse = [] if root.right is None else self.preorderTraversal(root.right)
    #    return [root.val] + left_traverse + right_traverse
    
    # iterative solution
    def preorderTraversal(self, root):
        result = []
        nodeStack = []
        
        while(len(nodeStack) != 0 or not root is None):
            if root is None:
                root = nodeStack.pop()
            
            result.append(root.val)
            
            if not root.right is None:
                nodeStack.append(root.right)
            
            root = root.left
            
        return result
