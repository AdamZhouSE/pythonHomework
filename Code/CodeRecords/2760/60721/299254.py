T=int(input())
for i in range(0,T):
    n,m=(map(int ,input().split(" ")))
    if(n%2==0):
        print(n/2*m)
    else:
        print(int(int(n/2)+1)*m)