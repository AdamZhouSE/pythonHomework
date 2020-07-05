nums=list(map(int,input().strip().split(",")))
count=1
for i in range(len(nums)-2):
    if nums[i]<nums[i+1]:
        count+=1
print(count)