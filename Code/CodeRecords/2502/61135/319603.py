n=int(input())
nums=[]
for i in range(n):
    nums.append(int(input()))
res=0
for i in range(1,n):
    res+=max(nums[i-1],nums[i])
print(res)