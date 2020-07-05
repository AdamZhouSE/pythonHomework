def dele(x,a,b):
    res=[]
    for i in range(0,len(x)):
        if x[i]>=a and x[i]<=b:
            pass
        else:
            res.append(x[i])
    return res
n,a=[int(x) for x in input().split(" ")]
x=[]
for i in range(n+1):
    x.append(i)
for p in range(a):
    b,c=[int(x) for x in input().split(" ")]
    x=dele(x,b,c)
print(len(x))