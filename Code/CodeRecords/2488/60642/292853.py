nums = eval(input())
nums.sort()
out = []
for i in range(int(len(nums)/2)+1):
    out.append(nums[i])
    if(i+1<len(nums)/2):
        out.append(nums[i+1+int(len(nums)/2)])
print(out)