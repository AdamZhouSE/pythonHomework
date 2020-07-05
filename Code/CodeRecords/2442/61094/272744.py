nums = input()
nums = nums.replace('[','')
nums = nums.replace(']','')
nums = nums.split(',')
size = len(nums)
if(size<2):
    print(0)
else:
    max = 0
    i = 0
    for num in nums:
        nums[i] = int(num)
        i += 1
    for i in range(0,size-1):
        for j in range(0,size-1):
            if(nums[j]>nums[j+1]):
                v = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = v
    for i in range(1,size):
        eax = int(nums[i]) - int(nums[i-1])
        if(eax>max):
            max = eax
    print(max)