def recursiveAdd(start,i,n):
    if i==n+1:
        return 0
    else:
        element=1
        for j in range(0,i):
            element=element*start
            start=start+1
        return element+recursiveAdd(start,i+1,n)

T=int(input())

for i in range(0,T):
    n=int(input())
    print(recursiveAdd(1,1,n))