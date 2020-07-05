nums=list(map(int,input().strip().split(",")))
nums.sort()
count=0
start=nums[0]
for i in nums[1:]:
    count+=i-start
print(count)