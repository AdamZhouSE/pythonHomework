def x(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    sum=0
    for i in range(len(res)):
        sum += res[i]
    return sum
n=int(input())
for p in range(n):
    a=int(input())
    b=x(a)
    if b<2*a:
        print(1)
    else:
        print(0)