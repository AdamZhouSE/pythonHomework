t=int(input())
for i in range(t):
    n=int(input())
    s=0
    while(n>0):
        if n%2==0:
            n=n/2
            s=s+1
        else:
            n=n-1
            s=s+1
    print(s)            
            
