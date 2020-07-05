def printSubset(n):
    for i in range(n,-1,-1):
        if i&n==i: print(i,'',end='')
    print()
t=int(input())
while t:
    printSubset(int(input()))
    t-=1