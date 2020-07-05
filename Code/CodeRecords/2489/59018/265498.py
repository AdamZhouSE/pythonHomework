def between(a,lower,upper):
    c=[]
    if len(a)==2:
        c.append(sum(a))
    else:        
        for i in range(len(a)-1):
            for j in range(i+1,len(a)-1):
                c.append(sum(a[i:j+1]))                
            c.append(sum(a[i:]))
    print(c)       

    
    
a=eval(input()) print(a)
lower=int(input()) print(lower)
upper=int(input()) print(upper)
between(a,lower,upper)
    