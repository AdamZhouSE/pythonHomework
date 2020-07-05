def remainder(n,numlist,k):
    mul=1
    for i in range(n):
        mul*=numlist[i]
    return mul%k
t=int(input())
for i in range(t):
    n=int(input())
    numlist=list(map(int,input().split(" ")))
    k=int(input())
    print(remainder(n,numlist,k))