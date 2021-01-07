class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        all_stairs = n
        for i in range(1, n):
            if all_stairs - i - (i+1) <0:
                return i
            else:
                all_stairs -= i