n=int(input())
for I in range(n):
    l=int(input())
    a=input().split()
    a.sort()
    res=0
    tmp=[]
    c=[]
    for i in range(0,l):
        if not a[i] in tmp:
            tmp.append(a[i])
            c.append(1)
        else:
            for j in range(len(tmp)):
                if tmp[j]==a[i]:
                    c[j]+=1
    #p#rint(a)
    #print(tmp)
    #print(c)
    for j in range(len(tmp)):
        if c[j]%2==1:
            res=tmp[j]
    print(res)
                
        