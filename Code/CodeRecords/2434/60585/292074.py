num=list(map(int, input().strip().split(' ')))
n=num[0]
m=num[1]
c=num[2]
res=[]
arr=list(map(int, input().strip().split(' ')))
for i in range(0,n-m+1):
    temp=arr[i:i+m]
    maxn=max(temp)
    minn=min(temp)
    if maxn-minn<=c:
        res.append(i+1)
if res:
    for i in res:
        print(i)
else:
    print('NONE',end='')
