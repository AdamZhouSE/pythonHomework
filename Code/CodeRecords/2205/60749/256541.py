def howmany(t):
    if t==2:
        return 1
    elif t==4:
        return 2
    else:
        sum=0
        for i in range(2,t-2,2):
            sum+=howmany(i)*howmany(t-i-2)
        sum+=2*howmany(t-2)
        return sum
n=int(input())
res=[]
for _ in range(n):
    res.append(int(input()))
for h in res:
    print(howmany(h),end="\n")