n=int(input())
for I in range(n):
    l=int(input())
    a=input().split()
    a=''.join(a)
    #print(a)
    res=[]
    for i in range(1,l+1):
        x=i
        for j in range(l-i+1):
            ja=True
            #print(j,j+x)
            tmp=a[j:j+x]
            tmp=list(tmp)
            tmp.sort()
            #print(tmp)
            for i in range(len(tmp)-1):
                if tmp[i]==tmp[i+1]:
                    ja=False
                    break
            if ja :
                res.append(tmp)
   # print(res)
    c=0
    for i in res:
        c+=len(i)
    print(c)