while(True):

    str0=input()
    list0=str0.split()
    m=int(list0[0])
    n=int(list0[1])
    if(m==0 or n==0):
        break
    t=1
    s=0
    sum=1
    i=m
    while(i<n):
        i=2*i+1
        s+=1
    
    for j in range(s-1,0,-1):
        t*=2
        sum=sum+t
    t*=2
    if(n-m*t>=0):
        sum=sum+n-(m*t)+1
    print(sum)
      