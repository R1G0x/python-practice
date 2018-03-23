class A:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    @property
    def z(self):
        return self.x + self.y

a = A(10, 15)
b = A('Hello', '!!!')
print(a.z)
print(b.z)