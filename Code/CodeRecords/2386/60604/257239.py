n=int(input())
def C(a,b):
    #a中取b个
    res=[]
    tmp=[i for i in range(b)]
    i=0
    res.append(tmp)
    while(tmp[0]!=a-b):
        print (tmp)
        #print(res)        
        #print(i)
        #res[i]=tmp
        print(res)
        for j in range(b-1,-1,-1):
            if tmp[j]!=a-b+j:
                tmp[j]+=1
                for k in range(j+1,b):
                    tmp[k]=tmp[k-1]+1
                break
        res.append(tmp)
        
    return res
for I in range(n):
    l=int(input())
    a=input().split()
    for i in range(l):
        a[i]=int(a[i])
    tag=int(input())
    res=0
    print(a)
    print(C(6,3))