def xx(x):
    res=[]
    for i in range(len(x)):
        res.append(x[i])
    return res
def judge(x,k):
    count=0
    for i in range(0,len(x)):
        if x[i]=="1":
            count += 1
    if count==k:
        return True 
    else:
        return False
n=int(input())
for p in range(n):
    a=[str(x) for x in input().split(" ")]
    k=int(a[1])
    b=xx(a[0])
    c=0
    for e in range(0,len(b)-1):
        for r in range(e+1,len(b)):
            if judge(b[e:r+1],k):
                c += 1
    for i in b:
        if i=="1" and k==1:
            c=c+1
    print(c)