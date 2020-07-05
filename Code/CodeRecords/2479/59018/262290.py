T=int(input())
for i in range(T):
    a=list(input())
    b=list(input())
    print(a)
    print(b)
    c=[]
    for j in range(len(a)):
        if a[j] not in b:
            c.append(a[j])
    for k in range(len(b)):
        if b[k] not in a:
            c.append(b[k])
    print(list(set(c)))    
            
            
        
    