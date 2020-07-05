nums = input()
nums = nums.replace('[','')
nums = nums.replace(']','')
nums = nums.split(',')
size = len(nums)
if(size<2):
    print(0)
else:
    max = 0
    nums = sorted(nums)
    for i in range(1,size):
        eax = int(nums[i]) - int(nums[i-1])
        if(eax>max):
            max = eax
    print(max)