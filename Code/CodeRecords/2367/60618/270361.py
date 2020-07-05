k=int(input())
re=0
n='1'
if k%2==0 or k%5==0:
    print(-1)
else:
    while re==0:
        if int(n)%k==0:
            re=1
        n+='1'
    print(len(n))
    
    
