n=int(input())
def findmin(l):
    mini=0
    m=l[0]
    for i in range(1,len(l)):
        if m>l[i]:
            mini=i
            m=l[i]
    return mini
for i in range(n):
    res=[]
    t=int(input())
    x=input().split()
    #print(x)
    tmp=[]
    for i in range(len(x)):
        x[i]=int(x[i])
        tmp.append(x[i])
    for i in range(len(tmp)):
        a=findmin(tmp)
        #rint(tmp)
        tmp[a]=10000000000000000000
        left=a
        right=a
        for i1 in range(a,-1,-1):
            if x[i1]>=x[a]:
                left=i1
            else:
                break
        for i1 in range(a,len(x)):
            if x[i1]>=x[a]:
                right=i1
            else:
                break
        res.append((right-left+1)*x[a])
        #print(res)
    max=0
    for i in res:
        if i>max:
            max=i
    print(max)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        