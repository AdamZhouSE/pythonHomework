nums=list(map(int,input()[1:-1].split(",")))
maximum=1
count=1
for i in range(1,len(nums)):
    if nums[i]>nums[i-1]:
        count+=1
        if count>maximum:
            maximum=count
    else:
        count=1
print(maximum)