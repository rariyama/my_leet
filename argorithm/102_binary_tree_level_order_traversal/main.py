import unittest
from typing import List

from binary_tree import TreeNode

class Solution:
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		if root == None:
			return []
		ans = list()
		child = list()
		parent = [root]
		while parent:
			child = parent
			parent = list()
			level = list()
			for x in child:
				level.append(x.val)
				if x.left:
					parent.append(x.left)
				if x.right:
					parent.append(x.right)
			ans.append(level)
			child = list()
		return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.data = [
            (TreeNode(
                    val=3,
                    left=TreeNode(
                        val=9,
                        left=None,
                        right=None,
                    ),
                    right=TreeNode(
                        val=20,
                        left=TreeNode(
                            val=15,
                            left=None,
                            right=None,
                        ),
                        right=TreeNode(
                            val=7,
                            left=None,
                            right=None,
                        ),
                    ),
                ),
                [
                    [3],
                    [9, 20],
                    [15, 7],
                ],
            ),
        ]

    def test_levelOrder(self):
        for [root, expected] in self.data:
            print(Solution().levelOrder(root))
            self.assertEqual(expected, Solution().levelOrder(root))


if __name__ == '__main__':
    unittest.main()
