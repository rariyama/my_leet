# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = list()
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = self._traverse(root)
        return ans
    
    def _traverse(self, root: TreeNode):
        if root is None:
            return self.ans
        if root.val:
            if root.left:
                self._traverse(root.left)
            if root.val:
                self.ans.append(root.val)
            if root.right:
                self._traverse(root.right)
        return self.ans