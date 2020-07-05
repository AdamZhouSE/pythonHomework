def between(a,lower,upper):
    c=a
    if len(a)==2:
        c.append(sum(a))
    else:        
        for i in range(len(a)-1):
            for j in range(i,len(a)-1):
                c.append(sum(a[i:j+1]))                
            c.append(sum(a[i:]))
    for k in c:
        count=0
        if lower<=k<=upper:
            count=count+1
    print(count)       
            


    
a=eval(input()) 
print(a)
lower=int(input()) 
print(lower)
upper=int(input()) 
print(upper)
between(a,lower,upper)
    