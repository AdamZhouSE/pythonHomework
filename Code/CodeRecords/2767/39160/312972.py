t = int(input())

for i in range(t):
    n=int(input())
    t=[0]*(n+1) 
    t[0]=1
    
    for i in range(3,n+1):
        t[i]+=t[i-3]
    for i in range(5,n+1):
        t[i]+=t[i-5]
    for i in range(10,n+1):
        t[i]+=t[i-10]
        
    print(t[n])    