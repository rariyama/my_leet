from typing import List
import unittest

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = list()
        if len(digits) == 1:
            num = digits[0]+1
            for d in str(num):
                ans.append(int(d))
            return ans

        if digits[-1] != 9:
            digits[-1] = digits[-1]+1
            return digits
        else:
            if digits == [9]*len(digits):
                return [1] + [0]*len(digits)
            else:
                idx = -1
                while digits[idx] ==9:
                    digits[idx] = 0
                    idx -= 1
                digits[idx] += 1
                return digits


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.test_case1 = [[1,2,3], [1,2,4]]
        self.test_case2 = [[0, 0], [0, 1]]
        self.test_case3 = [[0, 9], [1, 0]]
        self.test_case4 = [[0], [1]]
        self.test_case5 = [[9], [1, 0]]
        self.test_case6 = [[1,9], [2, 0]]
        self.test_case7 = [[9,9], [1, 0, 0]]

    def test_plus_one(self):
        sol = Solution()
        self.assertEqual(sol.plusOne(self.test_case1[0]), self.test_case1[1])
        self.assertEqual(sol.plusOne(self.test_case2[0]), self.test_case2[1])
        self.assertEqual(sol.plusOne(self.test_case3[0]), self.test_case3[1])
        self.assertEqual(sol.plusOne(self.test_case4[0]), self.test_case4[1])
        self.assertEqual(sol.plusOne(self.test_case5[0]), self.test_case5[1])
        self.assertEqual(sol.plusOne(self.test_case6[0]), self.test_case6[1])
        self.assertEqual(sol.plusOne(self.test_case7[0]), self.test_case7[1])

if __name__ == '__main__':
    unittest.main()