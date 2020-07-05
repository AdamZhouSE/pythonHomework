T=int(input())
for i in range(0,T):
    a1,a2=map(int,input().split())
    d=a2-a1
    N=int(input())
    res=a1+(N-1)*d
    print(res)