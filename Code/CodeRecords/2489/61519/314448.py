num=list(input().split(","))
num[0]=num[0][1:len(num)]
num[-1]=num[-1][0:-1]
for i in range(len(num)):
    num[i]=int(num[i])
lower=int(input())
upper=int(input())
n=len(num)
res=[]
tem=0
for i in range(n):
    tem=0
    for j in range(i,n):
        tem=0
        for k in range(i,j+1):
            tem=tem+num[k]
        res.append(tem)
res.sort()
ans=0
for i in range(len(res)):
    if res[i]>=lower and res[i]<=upper:
        ans+=1
print(ans)