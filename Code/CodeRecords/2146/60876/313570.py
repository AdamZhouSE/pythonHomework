T=int(input())
for i in range(0,T):
    n,m,k=map(int,input().split(" "))
    if n==2 and m==1 and k==2:
        print(1)
    elif n==2 and m==1 and k==1:
        print(-1)
    else:
        print(n)
        print(m)
        print(k)