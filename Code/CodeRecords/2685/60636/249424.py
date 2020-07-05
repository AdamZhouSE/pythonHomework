def sums(i):
    source=list(i)
    sum=0
    for x in source:
        sum=sum+int(x)
    return sum
t=int(input())
for j in range(t):
    n=int(input())
    x=0
    while(sums(x)!=n):
        x=x+1
    res=""
    for i in range(n):
        res=res+"0"
    res=str(x)+res
    print(int(res))
        