read = input()
read = read[1:len(read)-1]
nums = read.split(',')
nums = [int(nums[i]) for i in range(len(nums))]
h = 0

for i in range(0,len(nums)):
    times = 0
    for j in range(0,len(nums)):
        if nums[j]>=nums[i]:
            times = times+1
    if (times == nums[i]):
        h = times
if(h!=0):
    print(h)
else:
    print(1)