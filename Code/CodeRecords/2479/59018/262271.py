T=int(input())
for i in range(T):
    a=list(set(list(input())))
    b=list(set(list(input())))
    c=[]
    for j in range(len(a)):
        if a[j] not in b:
            c.append(a[j])
    for k in range(len(b)):
        if b[k] not in a:
            c.append(b[k])
    print(c)        
            
            
        
    