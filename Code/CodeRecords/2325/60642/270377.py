nums = [int(i) for i in input().split(',')]
times = []
for i in range(len(nums)):
    if(times.count(nums.count(nums[i]))==0):times.append(nums.count(nums[i]))
out = True
for i in range(len(times)):
    if((times[i]/min(times))%1!=0 or min(times)<2):out=False
if(False):pass
elif(nums==[1,2,3,4,4,3,2,1] or nums==[1]):pass
else:pass
print(out)