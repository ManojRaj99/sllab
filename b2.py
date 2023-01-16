from functools import reduce
from collections import Counter

f=open("1.txt")
content=f.read().split()
print(content)

countdic=Counter(content)
print(countdic)

s=sorted(countdic.items(),key=lambda x:x[1],reverse=True)
print(s[:10])

wordlength=[len(i) for i,j in s[:10]]

avg= (reduce(lambda x,y:x+y,wordlength))/len(wordlength)
print(avg)

coun=[i*i for i in wordlength if i%2!=0]
print(coun)