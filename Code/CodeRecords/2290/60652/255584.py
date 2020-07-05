T=int(input())
for i in range(0,T):
    N=int(input())
    l=list(map(int,input().split()))
    for n in range(0,len(l)-1):
        if l[n]>l[n+1]:
            print(l[n+1],end=" ")
        else:
            print(-1,end=" ")
    print(-1,end=" ")
    print()
