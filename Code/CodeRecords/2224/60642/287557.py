nums = [int(i) for i in input()]
out = ''
while(len(nums)>0):
    if(nums.index(max(nums))>0):
        temp = max(nums)
        nums[nums.index(max(nums))] = nums[0]
        nums[0] = temp
        out+=''.join(str(i) for i in nums)
        break
    else:
        out+=str(nums[0])
        nums.pop(0)
print(out)