# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s, t)
                
    def equals(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return s.val == t.val and self.equals(s.left, t.left) and self.equals(s.right, t.right)
    
    def traverse(self, s: TreeNode, t: TreeNode) -> bool:
        if s is not None:
            return self.equals(s, t) or self.traverse(s.left, t) or self.traverse(s.right, t)