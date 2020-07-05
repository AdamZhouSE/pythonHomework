n=int(input())
for I in range(n):
    l=int(input())
    a=input().split()
    for i in range(l):
        a[i]=int(a[i])
    k=int(input())
    tmp=[]
    res=0
    for i in range(l):
        for j in range(0,i):
            if not [a[i],a[j]] in tmp:
                tmp.append([a[i],a[j]])
        for j in range(i+1,l):
            if not [a[i],a[j]] in tmp:
                tmp.append([a[i],a[j]])
    for i in tmp:
        if i[0]-i[1]==k:
            res+=1
    print(res)