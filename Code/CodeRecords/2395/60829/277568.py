
def judge(x):
    for i in range(0,len(x)-1):
        if x[i]==x[i+1] and not x[i]==0:
            return True
    return False
def ch(x):
    res=[]
    for i in range(0,len(x)-1):
        if x[i]==x[i+1]:
            x[i]=x[i]*2
            x[i+1]=0
    for i in x:
        if not i==0:
            res.append(i)
    for i in range(len(x)-len(res)):
        res.append(0)
    return res
n=int(input())
for l in range(n):
    a=int(input())
    b=[int(x) for x in input().split(" ")]
    if judge(b):
        b=ch(b)
    res=""
    for i in range(0,len(b)):
        if i<len(b)-1:
            res=res+str(b[i])+" "
        else:
            res=res+str(b[i])
    print(res)