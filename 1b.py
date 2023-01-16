class Reverse:
    def __init__(self,string):
        self.string="".join(reversed(string.split()))

print("enter the 3 string")
arr=[]
vowel=[0,0,0]
dict={}
for i in range(3):
    a=Reverse(input())
    arr.append(a.string)
    for j in range(len(arr[i])):
        if arr[i][j].lower() in ['a','i','e','o','u']:
            vowel[i]+=1
    dict.update({arr[i]:vowel[i]})
print(sorted(dict.items(),key=lambda x:x[1],reverse=True))
