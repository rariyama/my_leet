class Solution:
    def __init__(self):
        self.ans = list()
        
    def fizzBuzz(self, n: int) -> List[str]:
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.ans.append("FizzBuzz")            
            elif i % 3 == 0:
                self.ans.append("Fizz")
            elif i % 5 == 0:
                self.ans.append("Buzz")
            else:
                self.ans.append(str(i))
        return self.ans