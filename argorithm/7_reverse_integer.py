class Solution:
    def __init__(self):
        self.min = -2**31
        self.max = 2**31-1
    
    def _is_not_in_range(self, ans: int) -> bool:
        if ans not in range(self.min, self.max):
            return True
        else:
            return False
            
    def reverse(self, x: int) -> int:
        if x > 0:
            ans = int(str(x)[::-1])
            if self._is_not_in_range(ans) is True:
                return 0
            else:
                return ans
        elif x < 0:
            ans = int(str(x*-1)[::-1]) * -1
            if self._is_not_in_range(ans) is True:
                return 0
            else:
                return ans
        elif x == 0:
            return 0
        