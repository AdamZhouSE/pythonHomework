nums = eval(input())
times = []
for i in range(len(nums)):
    if(times.count(nums.count(nums[i]))==0):times.append(nums.count(nums[i]))
out = True
for i in range(len(times)):
    if((times[i]/min(times))%1!=0):out=False
print(out)