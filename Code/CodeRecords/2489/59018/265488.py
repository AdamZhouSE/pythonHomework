def between(a,lower,power):
    c=[]
    if len(a)==2:
        c.append(sum(a))
    else:        
        for i in range(len(a)-1):
            for j in range(i+1,len(a)-1):
                c.append(sum(a[i:j+1]))                
            c.append(suma[i:])
    print(c)       

    
    
a=eval(input())
lower=int(input())
upper=int(input())
between(a,lower,power)
    