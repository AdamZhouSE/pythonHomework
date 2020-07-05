t=int(input())
for i in range(t):
    inlist=list(input())
    l=len(inlist)

    ss=[]
    for i in range(l):
        s=1
        for j in range(i,l-1):
            if inlist[j+1]>inlist[j]:
                s=s+1
            else:
                ss.append(s)
                break
                
    print(6)     