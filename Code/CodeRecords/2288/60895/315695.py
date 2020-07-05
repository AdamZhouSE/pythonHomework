while True:
    m,n=input().split(' ')
    m=int(m)
    n=int(n)
    
    if m!=0 and n!=0:
        t=1
        s=0
        sum=1
        i=m
        while i<n:
            i=2*i+1
            s+=1
        for j in range(s-1,0,-1):
            t=t*2
            sum=sum+t
        t=t*2
        if(n-m*t>=0):
            sum=sum+n-(m*t)+1
        print(sum)
    
    
    
    
    
    
    
    
    