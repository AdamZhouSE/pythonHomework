def sor(a,b):
    c=[]
    for i in range(len(a)):
        if a[i] not in b:
            c.append(a[i])
            del a[i]
            
    c.sort()
    d=[]
    for j in range(len(b)):
        for k in range(len(a)):
            if b[j]==a[k]:
                d.append(a[k])
    result=d+c
    print(result)
    
        
    
    
    
    
a=eval(input())
b=eval(input())
print(a)
print(b)
sor(a,b)