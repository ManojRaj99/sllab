from functools import reduce

old=[]
print('enter 6 elements')
for i in range (6):
    old.append(int(input()))

new=[(lambda x: 3*x)(x) for x in old]
print(new)

print(reduce(lambda a,b:a+b,old))
print(reduce(lambda a,b:a+b,new))