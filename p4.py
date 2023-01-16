history=[]
def ctok(temp):
    return temp+273
def ktoc(temp):
    return temp-273
def ctof(temp):
    return (temp*9/5)+32
def ftoc(temp):
    return (temp-32)*5/9

while 1:
    c=int(input("1.ctok\n2.ktoc\n3.ctof\n4.ftoc\n5.ftok\n6.ktof\n7.history\n8.exit\nenter ur choice\n"))

    if c==8:
        exit()
    if c==7:
        print(history)
        continue

    temp=int(input("enter the temperature"))
    if c==1:
        cov=ctok(temp)
    if c==2:
        cov=ktoc(temp)
    if c==3:
        cov=ctof(temp)
    if c==4:
        cov=ftoc(temp)
    if c==5:
        cov=ctok(ftoc(temp))
    if c==6:
        cov=ctof(ktoc(temp))
    
    print(cov)
    conversion=(temp,cov)
    history.append(conversion)
   