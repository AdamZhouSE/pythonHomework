t=int(input())
for i in range(t):
    mn=input().split(' ')
    m=int(mn[0])
    n=int(mn[1])
    
    
    def f(x):
        if x==0:
            return 1
        res=x
        while x>1:
            x-=1
            res*=x
        return res
    
    
    ans=f(n+m-2)//(f(n-1)*f(m-1))
    print(ans)