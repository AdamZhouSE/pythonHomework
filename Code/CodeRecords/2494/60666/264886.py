nums=eval(input())
count=0
for i,j in zip(range(len(nums)),range(len(nums))):
    if i<j and nums[i]>2*nums[j]:
        count+=1
print(count)