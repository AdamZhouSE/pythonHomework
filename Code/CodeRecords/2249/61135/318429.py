T=int(input())
nums=list()
for a in range(0,T):
    temp=eval("["+input()+"]")
    nums.append(temp)
xy=0
xz=0
for i in range(0,len(nums)):
    t=0
    for j in range(0,len(nums)):
        if(nums[j][i]>t):
            t=nums[j][i]
        if(nums[j][i]!=0):
            xy+=1
    xz+=t
yz=0
for i in nums:
    yz+=max(i)
print(xy+xz+yz)