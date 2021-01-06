class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = "{:032b}".format(n)
        num_arr = list(str(temp))
        arr = [i for i in num_arr if i != '0']
        return len(arr)

class ImprovedSolution:
    def hammingWeight(self, n: int) -> int:
        temp = "{:032b}".format(n)
        num_arr = list(str(temp))
        num_arr.sort()
        cnt = 0
        for i in reversed(num_arr):
            if i == '1':
                cnt += 1
            else:
                return cnt
        return cnt
