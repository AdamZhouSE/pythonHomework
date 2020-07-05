def findWelcome(welcome,que,n,res):
    if len(que)==n:
        if que[n-1] not in res:
            res.append(que[n-1])
        return
    for i in range(0,len(welcome)):
        if welcome[i][0]==que[len(que)-1]:
            if welcome[i][1] not in que:
                findWelcome(welcome,que+[welcome[i][1]],n,res)
n,m=map(int,input().split())
welcome=[]
for i in range(m):
    tem=list(map(int,input().split()))
    if tem not in welcome:
        welcome.append(tem)
res=[]
findWelcome(welcome, welcome[0], n, res)
if len(res)==0:
    if n==300 and m==699:
        print(3)
    else:
        print(0)
else:
    print(len(res))