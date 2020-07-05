nums=eval(input())
for i in range(len(nums)-1):
    ptr=i+1
    while(nums[i]==nums[ptr] and ptr<len(nums)-1):
        ptr+=1
    nums[i+1],nums[ptr]=nums[ptr],nums[i+1]
for i in range(len(nums)-1):
    j=len(nums)-1-i
    ptr=j-1
    while(nums[j]==nums[ptr] and ptr>=0):
        ptr-=1
    nums[j-1],nums[ptr]=nums[ptr],nums[j-1]
print(nums)