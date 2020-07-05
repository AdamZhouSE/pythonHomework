nandk=input().split(" ")
n=int(nandk[0])
k=int(nandk[1])
a=[]
pos=[]
for _ in range(k):
    nums=list(map(int, input().split(" ")))
    temp=[]
    a.append(nums)
    for h in nums:
        temp.append(nums.index(h))
    pos.append(temp)
dp=[]
for i in range(n):
    dp.append(1)
for i in range(n):
    for j in range(i):
        x=a[0][i]
        y=a[0][j]
        flag=1
        for t in range(1,k):
            if pos[t][x-1]<pos[t][y-1]:
                flag=0
                break
        if flag==1:
            dp[x-1]=max(dp[x-1],dp[y-1]+1)
print(max(t for t in dp))