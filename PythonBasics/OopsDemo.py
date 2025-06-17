# classes are user defined blueprint or prototype
# Class calculator so it have sum, multiplication, addition

class Calculator:
    num = 100 #class variable where as if you create variable within contructor that is called instance variable

    def __init__(self, a, b): #contructor
        self.firstnumber =a
        self.secondnumber=b
        print("contructor is called automatically")

    def getData(self):
        print("Anything in method")

    def summation(self):
        return self.firstnumber+self.secondnumber +Calculator.num

obj=Calculator(2,3)   # syntax to create obj in class
obj.getData()
print(obj.summation())