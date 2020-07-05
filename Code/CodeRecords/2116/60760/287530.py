n=int(input())
primes=list(map(int,input().split(',')))
x=1
res=[]
while len(res)<n:
    y=x
    for i in primes:
        while int(x/i)==x/i:
            x=int(x/i)

    if x==1:
        res.append(y)
    x=y+1
print(res[n-1])