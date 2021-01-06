class Solution:
    def hammingWeight(self, n: int) -> int:
        temp = "{:032b}".format(n)
        num_arr = list(str(temp))
        arr = [i for i in num_arr if i != '0']
        return len(arr)