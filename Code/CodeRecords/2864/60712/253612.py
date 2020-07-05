n = int(input())
nums = list(map(int,input().split()))
nums.sort()
l = [0]*(max(nums)+1)
pre = nums[0]
s = 0
for i in range(0,n):
    if nums[i]==pre:
        s+=1
    else:
        l[pre]=s*pre
        s=1
        pre = nums[i]
    if i==n-1:
        l[pre]=s*pre
if max(nums)==1:
    print(l[1])
else:
    v = [0]*(max(nums)+1)
    for i in range(2,len(v)):
        v[i]=max(v[i-1],v[i-2]+l[i])
    print(v[len(v)-1]+1)

