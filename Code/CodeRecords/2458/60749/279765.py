nandk=input().split(" ")
n=int(nandk[0])
k=int(nandk[1])
a=[]
pos=[]
nums2=list(map(int, input().split(" ")))
temp2=[]
a.append(nums2)
for h in nums2:
    temp2.append(nums2.index(h))
pos.append(temp2)
for _ in range(k-1):
    nums=list(map(int, input().split(" ")))
    temp=[]
    a.append(nums)
    for h in nums2:
        temp.append(nums.index(h))
    pos.append(temp)
dp=[]
for i in range(n):
    dp.append(1)
for i in range(n):
    for j in range(i):
        x=a[0][i]
        index_x=nums2.index(x)
        y=a[0][j]
        index_y=nums2.index(y)
        flag=1
        for t in range(1,k):
            if pos[t][index_x]<pos[t][index_y]:
                flag=0
                break
        if flag==1:
            dp[i]=max(dp[i],dp[j]+1)
print(max(t for t in dp))