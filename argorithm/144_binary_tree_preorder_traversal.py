# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = list()
    
    def traverse(self, root: TreeNode):
        if root is not None:
            self.ans.append(root.val)
            if root.left is not None:
                self.traverse(root.left)
            if root.right is not None:
                self.traverse(root.right)
        return

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.ans
        self.ans.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
        return self.ans
