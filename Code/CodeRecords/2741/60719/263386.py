nums = input()
nums = nums[1:len(nums)-1].split(",")
length = 1
start = 0
maxstart = 0
maxlen = 1
for i in range(1, len(nums)):
    if int(nums[i]) >= int(nums[i-1]):
        if length == 1:
            start = i-1
        length += 1
    else:
        if length > maxlen:
            maxlen = length
            maxstart = start
        length = 1
print(maxlen)