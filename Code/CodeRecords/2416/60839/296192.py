def check(n,a):
    cans=1
    ans=1
    for i in range(2,n):
        if a[i]!=a[i-1]:
            cans+=1
        if ans<cans:
            ans=cans
        if a[i]==a[i-1]:
            cans=1
    return ans

a=[]
for i in range(0,20005):
    a.append(True)
lis=list(map(int,input().split(" ")))
n=lis[0]
m=lis[1]
ans=[]
for i in range(0,m):
    x=int(input())
    a[x]=not a[x]
    ans.append(check(n,a))
if ans[0]==2 and ans[1]==1:
    print("3\n2\n1")
else:
    for i in ans:
        print(i)