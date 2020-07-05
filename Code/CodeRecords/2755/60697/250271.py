t=int(input())
sizes=[]
a=[]
b=[]
for i in range(t):
    sizes.append(list(map(int,input().split(' '))))
    a.append(list(map(int,input().split(' '))))
    b.append(list(map(int,input().split(' '))))
for i in range(t):
    asize=sizes[i][0]-1
    bsize=sizes[i][1]-1
    aa=a[i]
    bb=b[i]
    all=asize+bsize
    res=[]

    for j in range(all+1):
        tmp=0
        for k in range(j+1):
            if(k<=asize and j-k<=bsize):
                tmp+=aa[k]*bb[j-k]
        res.append(tmp)
    print(" ".join(list(map(str,res))))