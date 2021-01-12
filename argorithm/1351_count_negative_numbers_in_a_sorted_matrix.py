import unittest
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for arr in grid:
            ans += len([i for i in arr if i < 0])
        return ans
            

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_data1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
        self.collect1 = 8
        self.test_data2 = [[3,2],[1,0]]
        self.collect2 = 0


    def test_count_negatives(self):
        res = Solution().countNegatives(self.test_data1)
        self.assertEqual(res, self.collect1)

        res = Solution().countNegatives(self.test_data2)
        self.assertEqual(res, self.collect2)

if __name__ == '__main__':
    unittest.main()
