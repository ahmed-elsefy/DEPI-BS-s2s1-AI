class Calculator:
    def __init__(self,x,y):
                    self.x = x
                    self.y = y
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b