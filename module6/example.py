import math

class Calculate:
    def __init__(self,a,b,c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        result = self.a + self.b + self.c
        print(result)
    
    def factorial(self):
        answer = math.factorial(self.b)
        print(answer)

    
con = Calculate(4,5,8)
con.sum()
con.factorial()
