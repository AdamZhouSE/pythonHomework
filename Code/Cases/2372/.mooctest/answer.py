def solution():
    n,x,y=map(int,input().split())
    #print(n,x,y)
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    diff =[abs(x - y) for x, y in zip(a, b)]
    index=[i for i in range(n)]
    zipped = zip(diff,index)
    z = [x for _, x in sorted(zipped)]
    
    sum=0
    for i in reversed(z):
        if a[i]>=b[i] and x>0:
            x=x-1
            sum=sum+a[i]
        elif a[i]>=b[i]:
            y=y-1
            sum=sum+b[i]
        elif b[i]>=a[i] and y>0:
            y=y-1
            sum=sum+b[i]
        elif b[i]>=a[i]:
            x=x-1
            sum=sum+a[i]
            
    print(sum)
        
        
        
t=int(input())
for i in range(t):
    solution()