n=int(input())
for i in range(n):
    
    x=input().split()
    x=int(x[2])
    a=input().split()
    b=input().split()
    for i in b:
        a.append(i)
    for i in range(len(a)):
        a[i]=int(a[i])
    
    a.sort()
    print(a[x-1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    