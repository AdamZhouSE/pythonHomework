T=int(input())
for a in range(0,T):
    n=int(input())
    count=0
    while(n>0):
        if(n%2==0):
            n=n//2
        else:
            n=n-1
        count=count+1
    print(count)    
    