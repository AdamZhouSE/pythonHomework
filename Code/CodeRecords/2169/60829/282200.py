def r(x):
    res=[]
    if len(x)==1:
        return x
    for i in range(2,len(x)):
        if x[i]=="+":
            a=int(x[i-1])+int(x[i-2])
            for j in x[0:i-2]:
                res.append(j)
            res.append(a)
            for j in x[i+1:len(x)]:
                res.append(j)
            return res
        elif x[i]=="-":
            a=int(x[i-2])-int(x[i-1])
            for j in x[0:i-2]:
                res.append(j)
            res.append(a)
            for j in x[i+1:len(x)]:
                res.append(j)
            return res
        elif x[i]=="*":
            a=int(x[i-1])*int(x[i-2])
            for j in x[0:i-2]:
                res.append(j)
            res.append(a)
            for j in x[i+1:len(x)]:
                res.append(j)
            return res
        elif x[i]=="/":
            a=int(x[i-2])//int(x[i-1])
            for j in x[0:i-2]:
                res.append(j)
            res.append(a)
            for j in x[i+1:len(x)]:
                res.append(j)
            return res
def rr(x):
    res=[]
    for i in range(0,len(x)):
        res.append(str(x[i]))
    return res
n=int(input())
for p in range(n):
    s=rr(str(input()))
    while len(s)>3:
        s=r(s)
    a=r(s)[0]
    print(a)