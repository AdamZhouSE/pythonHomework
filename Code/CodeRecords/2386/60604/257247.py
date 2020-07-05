n=int(input())
def C(x,a,b):
    #a中取b个
    res=[]
    tmp=[i for i in range(b)]
    i=0
    res.append(tmp)
    while(tmp[0]!=a-b):
        aaa=tmp
        #print (tmp)
        #print(res)        
        #print(i)
        #res[i]=tmp
        #print(res)
        for j in range(b-1,-1,-1):
            if tmp[j]!=a-b+j:
                tmp[j]+=1
                for k in range(j+1,b):
                    tmp[k]=tmp[k-1]+1
                break
        tmp1=[]
        for i in tmp:
            tmp1.append(x[i])
        res.append(tmp1)
        
    res[0]=aaa    
    return res
for I in range(n):
    l=int(input())
    a=input().split()
    for i in range(l):
        a[i]=int(a[i])
    tag=int(input())
    res=0
    #print(a)
    tmp=C(a,l,4)
    tmp1=[a[0],a[1],a[2],a[3]]
    tmp[0]=tmp1
    #print(tmp)
    for i in tmp:
        k=0
        for j in i:
            k+=j
        if k==tag:
            res=1
            break
    print(res)
    