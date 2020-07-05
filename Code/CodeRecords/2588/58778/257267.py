n=int(input())
for i in range(n):
    m=int(input())
    k=m
    z=0
    if(m==1):
        z=1
    s=1
    temp=[]
    while(m!=1):
        for j in range(2,m+1):
            if(m%j==0):
                temp.append(j)
                m=int(m/j)
                break
    numlist=list(str(k))
    c=0
    for d in numlist:
        c=c+int(d)
    x=0
    for d in temp:
        if(d>=10):
            l=list(str(d))
            for r in l:
                x=x+int(r)
        else:
            x=x+d
    if(z==1):
        print(1)
    else:
        if(c==x and len(temp)!=1):
            print(1)
        else:
            print(0)

 
    