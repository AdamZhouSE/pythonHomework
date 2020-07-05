num=list(input().split(","))
num[0]=num[0][1:len(num[0])]
num[-1]=num[-1][0:-1]
for i in range(len(num)):
    num[i]=int(num[i])
n=int(input())
res=[]
for i in range(n):
    for j in range(i,n):
        tem=0
        for k in range(i,j+1):
            if k==n:
                break
            tem+=num[k]
        if tem>=n:
            res.append(tem)
            break
if len(res)==0:
    print(-1)
else:
    res.sort()
    print(res[0])