def smallernums(a):
    b=[]
    for i in range(len(a)-1):
        count=0
        for j in range(i,len(a)):
            if a[j]<a[i]:
                count=count+1
        b.append(count)        
    b.append(0)
    print(b)
    
    
a=eval(input())
smallernums(a)