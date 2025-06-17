#whatever you declare in parent class, you can use in child class that is inheritance
# if there is contructor in parent class then you have to class that contructor in child class too
from OopsDemo import Calculator


class ChildImpi(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2,10)

    def getComplete(self):
        return self.num2+ self.num +self.summation()


obj=ChildImpi()
print(obj.getComplete())