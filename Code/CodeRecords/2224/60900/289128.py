n = input()
nums =[]
for i in range(0,len(n)):
    nums.append(int(n[i]))
l = len(nums)
bb=""
def baba(nums,bb):
    if len(bb)==l:
        return bb

    if nums[0] !=max(nums):
        index=nums.index(max(nums))
        temp = nums[0]
        nums[0]=max(nums)
        nums[index]=temp
        for i in range(0,len(nums)):
            bb+=str(nums[i])
        return bb
    else:
        bb+=str(nums[0])
        del nums[0]
        bb=baba(nums,bb)
        return bb

print(baba(nums,bb))