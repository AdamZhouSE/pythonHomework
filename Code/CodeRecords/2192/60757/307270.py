def pr(m,n,con):
    if n<=m:
        print(n,end=' ')
        if con==1:    
            n=n-5
            if n<=0:
                con=0
        else:
            n=n+5
        pr(m,n,con)
t=int(input())
for i in range(t):
    n=int(input())
    pr(n,n,1)
    print()