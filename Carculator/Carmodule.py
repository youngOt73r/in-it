print ("연산중입니다.\n")
class Carc:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def plus(self):
        return self.a + self.b
    def minus(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b