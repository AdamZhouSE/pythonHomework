n = int(input())
nums=[]
result =0
for i in range(0,n):
    nums.append(int(input()))
for i in range(0,n-1):
    result+=max(nums[i],nums[i+1])
print(result)