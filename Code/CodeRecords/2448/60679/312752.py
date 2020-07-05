read = input()
read = read[1:len(read) - 1]
nums = read.split(',')
nums = [int(nums[i]) for i in range(len(nums))]
h = 0

for i in range(0, max(nums)+1):
    times = 0
    no = 0
    for j in range(0, len(nums)):
        if nums[j] >= i:
            times = times + 1
        if nums[j] <= i:
            no = no + 1
    if (times <= i and times > h):
        h = times
        if((no + h) !=len(nums)):
            times = times+1

print(h)