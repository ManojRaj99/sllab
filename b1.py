class Reverse:
    def __init__(self,string):
        self.string=" ".join(reversed(string.split()))

print("enter three string here")
arr=[]
vowel=[0,0,0]
dect={}
for i in range(3):
    a=Reverse(input())
    arr.append(a.string)
    for j in range(len(arr[i])):
        if arr[i][j].lower() in ['a','e','i','o','u']:
            vowel[i]+=1
    dect.update({arr[i]:vowel[i]})        

print(sorted(dect.items(),key=lambda x:x[1],reverse=True))
