class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > 0:
            ans = int(str(x)[::-1])
            if x == ans:
                return True
            else:
                return False
        elif x < 0:
            ans = str(x*-1)[::-1]+ '-'
            if x == ans:
                return True
            else:
                return False
        elif x == 0:
            return True