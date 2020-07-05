def rightestDiff(m,n):
    if m==n:
        print(-1)
        return
    for i in range(0,31):
        mbit=1&(m>>i)
        nbit=1&(n>>i)
        if mbit!=nbit:
            print(i+1)
            return
        
t=int(input())
while t:
    line=[int(x) for x in input().split()]
    m=line[0]
    n=line[1]
    rightestDiff(m,n)
    t-=1