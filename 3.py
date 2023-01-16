class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def findarea(self):
        return int(self.length)*int(self.breadth)

obj=rectangle(10,5)
print('area='+str(obj.findarea()))

n=int(input('enter length'))
m=int(input('enter breadth'))

obj1=rectangle(n,m)
print('area='+str(obj1.findarea()))       