li = []
n = input('enter the no of elements')
print('enter'+n+'nubers')
for i in range(int(n)):
    li.append(int(input()))

while 1:
    c=int(input('1.insert\n2.delete\n3.find\n4.minmax\n5.display\6.exit\n enter ur choice\n'))

    if c==1:
        li.insert(int(input('enter pos')),int(input('enter element')))
        print(li)
    elif c==2:
        try:
            li.remove(int(input('enter the element')))
            print(li)
        except:
            print("elem no found")
    elif c==3:
        try:
            pos=li.index(int(input('enter the element')))
            print("the element found at"+str(pos))
        except:
            print("elemnt not found")
    elif c==4:
        print("max="+str(max(li)))
        print("min="+str(min(li)))
    elif c==5:
        print(li)
    
    else:
        break

