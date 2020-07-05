n=int(input())
for i in range(n):
    l=0
    m=int(input())
    s=input()
    slist=s.split( )
    nl=[]
    for i in slist:
        nl.append(int(i))
    for i in range(m-1):
        sum=0
        for j in range(i,m):
            sum=sum+nl[j]
            if(sum==0):
                l=1
                break
        if(l==1):
            break
    if(l==1 or nl[len(nl)-1]==0):
        print('Yes')
    else:
        print('No')