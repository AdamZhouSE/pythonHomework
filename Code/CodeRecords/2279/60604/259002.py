n=int(input())
def add(a):
    res=0
    for i in a:
        res+=i
    return res
for I in range(n):
    x=input().split()
    l=int(x[0])
    tag=int(x[1])
    a=input().split()
    #print(a)
    #print(tag)
    for i in range(l):
        a[i]=int(a[i])
    res=-1
    f=True
    roo=[]

    for i in range(l-1):
        for j in range(i+1,l):
            tmp=add(a[i:j+1])
            if tmp==tag:
                res=str(i+1)+' '+str(j+1)
                roo.append(res)
                #print(roo)
                f=False            
    if len(roo)>0:
        print(roo[0])
    else:print(-1)