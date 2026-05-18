class CalculatorLogic:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)
        return self.expression
    
    def clear(self):
        self.expression=""
        return self.expression
    
    def backspace(self):
        self.expression=self.expression[:-1]
        return self.expression
    def calculate(self):
        try:
            self.expression= str(eval(self.expression))
            return self.expression
        except:
            self.expression=""
            return "Error"
        
        