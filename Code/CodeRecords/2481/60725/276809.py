n=int(input())
for i in range(n):
    s=input().split()
    
    r=input().split()
    c=set(s)
    t=set(r)
    y=c&t
    
    
    print(len(y))
    
    

