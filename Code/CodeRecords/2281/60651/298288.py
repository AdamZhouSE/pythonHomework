t=int(input())
for i in range(t):
    l=int(input())
    inlist=input().split()
    inlist=[int(x) for x in inlist]
    a=[]
    for i in range(l):
        if i!= l-1:
            flag=1
            for j in range(i,l):
                if inlist[i]<inlist[j]:
                    flag=0
            if flag==1:        
                a.append(inlist[i])
        if i == l-1:
            a.append(inlist[i])
    a=[str(x) for x in a]
    print(" ".join(a))        
            