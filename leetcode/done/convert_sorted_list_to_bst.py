# Given a singly linked list where elements are sorted in ascending order, 
# convert it to a height balanced BST.

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        arr = self.to_arr(head)
        return self.sortedArrayToBST(arr)
        
    def to_arr(self, head):
        l = []
        while (head != None):
            l.append(head.val)
            head = head.next
        return l
        
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

