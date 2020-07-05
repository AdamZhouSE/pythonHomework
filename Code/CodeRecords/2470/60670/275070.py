t=int(input())
for tt in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(2,-1,-1):
        for j in range(0,3):
            print(a[i*3+j],end=' ')
    print()