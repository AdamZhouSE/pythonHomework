def copy(a):
    t=[0]*len(a)
    for i in range(len(a)):
        t[i]=a[i]
    return t
n=int(input())
arr=list(map(int,input().split()))
ans=[]
for i in range(n):
    l=[]
    for j in range(1,n-i+1):
        tem=copy(arr)
        begin=i
        end=j
        for t in range(i,j):
            if tem[t]==0:
                tem[t]=1
            else:
                tem[t]=0
        count=0
        for t in tem:
            if t==1:
                count+=1
        l.append(count)
    l.sort()
    ans.append(l[-1])
ans.sort()
print(ans[-1])

