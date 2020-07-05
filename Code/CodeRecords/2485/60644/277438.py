t=int(input())
for i in range(0,t):
    n=int(input())
    a=input().split()
    res=[]
    for j in range(0,n):
        res=res+[list(a[j])]
    for j in range(0,n):
        res[j]=set(res[j])
    arr=[]+res
    p=[]
    for j in range(0,n):
        for k in range(0,j):
            if res[j]==res[k]:
                res[j]=-1
                break
    for j in range(0,n):
        if res[j]!=-1:
            p=p+[res[j]]
    for j in range(0,len(p)):
        p[j]=arr.count(p[j])
    for j in range(0,len(p)):
        for k in range(0,len(p)-1):
            if p[k]>p[k+1]:
                p[k],p[k+1]=p[k+1],p[k]
    s=''
    for j in range(0,len(p)):
        s=s+' '+str(p[j])
    print(s[1:])
