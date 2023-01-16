class student:
    def __init__(self):
        self.name=input('enter the name')
        self.age=input("enter the age")
        self.marks=[]
    def accept(self):
        for i in range(3):
            self.marks.append(input('enter subject'+str(i+1)+'marks'))
    def display(self):
        print('name'+str(self.name))
        print("age"+str(self.age))
        print("marks of 3 sub")
        print(self.marks)
s=student()
s.accept()
s.display()

s1=student()
s1.accept()
s1.display()