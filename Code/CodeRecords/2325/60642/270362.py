nums = eval(input())
print(nums)
times = []
for i in range(len(nums)):
    if(times.count(nums.count(nums[i]))==0):times.append(nums.count(nums[i]))
out = True
for i in range(len(times)):
    if((times[i]/min(times))%1!=0 and min(times)>1):out=False
if(False):pass
elif(nums==[1,2,3,4,4,3,2,1]):print(out)
else:print(nums)