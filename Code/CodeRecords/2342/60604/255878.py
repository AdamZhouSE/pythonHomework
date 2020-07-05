
n=input()
for i in range(int(n)):
    x=input().split()
    l=int(x[0])
    s=int(x[1])
    a=input().split()
    tmp=[]
    res=[]
    for j in range(0,l,s):
        #print(j)
        
        if l-1-j>=s:
            for k in range(s):
                tmp.append(a[j+k])
            tmp.reverse()
        else:
            for k in range(j,l):
                tmp.append(a[k])
            tmp.reverse()
        for k in tmp:
            res.append(k)
        tmp=[]
    for j in res:
        print(j,end=" ")
    print()
                
        