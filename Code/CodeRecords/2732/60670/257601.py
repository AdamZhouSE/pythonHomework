t=int(input())
for k in range(0,t):
    a,b,c=map(int,input().split())
    print((a**b)%c)
    '''a=a%c
    ans=1
    for i in range(0,b):
        ans=(ans*a)%c
    print(ans)
    '''