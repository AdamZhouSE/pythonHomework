t=int(input())
for i in range(t):
    i=input()
    inlist=list(input())
    l=len(inlist)
    f=0
    for i in range(l):
        s=0
        for j in range(l):
            if inlist[i]!=inlist[j] and i!=j:
                s=s+1
        if s==l-1:   
            f=1
            print(inlist[i])     
            break    
                
    if f==0:
        print(-1)
                