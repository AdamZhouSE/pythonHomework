import math
def quanpai(a,times):
    if(times==0):
        return [a]
    res=[]
    res.append(a)
    for i in range(0,len(a)):
        for r in range(0,len(a)):
            li=a.copy()
            if(i!=r):
                li[i]=a[r]
                li[r]=a[i]
            res.append(li)
            res.extend(quanpai(li,(times-1)))
        if(times==0):
            break
    res.sort()
    re=[]
    for i in range(0,len(res)):
        if len(re)==0:
            re.append(res[0])
        else:
            if(res[i-1]==res[i]):
                continue
            else:
                re.append(res[i])
    return re

def isa(a):
    b=int(math.sqrt(a))
    c=math.sqrt(a)
    if((c-b)<=0.001):
        return 1
    else:
        return 0
def com(res):
    cu=int(res[0])
    num=1
    for i in range(1,len(res)):
        if(isa((cu+int(res[i])))==1):
            num+=1
            cu=int(res[i])
        else:
            return 0
    if(num==len(res)):
        return int(1)
    else:
        return int(0)
n=input()
b=list(eval(n))
cu=int(b[0])
num=0
flag=1
li1=quanpai(b,len(b))
for i in range(len(b)):
    if(b[i]!=b[0]):
        flag=0
if(flag==1):
    if(isa((int(b[0])*2))==0):
        print(0)
        exit()
    print(1)
    exit()
for i in range(len(li1)):
        num=num+ com(li1[i])
print(num)