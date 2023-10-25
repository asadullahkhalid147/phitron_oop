class A:
    def __init__(self, value):
        value = 3
        self.value = value


    def change(self):
        self.value = 12




ans = []
a = A(100)
ans.append(a.value)
a.change()
ans.append(a.value)
print(ans)