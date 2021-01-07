class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ans = Counter(t) - Counter(s)
        return sum(ans.values())