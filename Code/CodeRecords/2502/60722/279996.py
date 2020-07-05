n=int(input())
nums=[]
result=0
for i in range(n):
    nums.append(int(input()))
for i in range(1,n):
    result+=max(nums[i-1],nums[i])
print(result)