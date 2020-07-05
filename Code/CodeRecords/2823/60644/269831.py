def f(arr,dex,k,n,res):
    if dex!=k-1:
        for i in range(1, n + 1):
            arr[dex] = i
            res=f(arr, dex + 1, k, n, res)
    else:
        for i in range(1,n+1):
            arr[k-1]=i
            a=[]+arr
            res=res+[a]


    return res







t=input().split()
n=int(t[0])
k=int(t[1])
a=[1]*k
s=0
res=[]
arr=[0]*k
ans=f(arr,0,k,n,res)
for i in range(0,len(ans)):
    p=True
    for j in range(0,k-1):
        if ans[i][j+1]%ans[i][j]!=0:
            p=False
            break
    if p:
        s+=1
print(s%1000000007)
