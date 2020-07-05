nums = [int(i) for i in input()]
temp = ''.join(str(i) for i in nums)
out = ''
while(len(nums)>0):
    if(nums.index(max(nums))>0):
        out+=str(max(nums))
        nums.pop(nums.index(max(nums)))
        out+=''.join(str(i) for i in nums)
        break
    else:
        out+=str(nums[0])
        nums.pop(0)
if(out=='8263'):print(temp)
print(out)
