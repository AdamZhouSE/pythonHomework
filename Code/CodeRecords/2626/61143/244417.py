nums = eval(input())
nums = list(nums)
numk1 = [1]
numk2 = [1]
#print(nums)
max_mul = 0
count = 0
tag = 0
for i in range(len(nums)-3):
    for i in range(1,len(nums)-1):
        if(nums[i-1]*nums[i]*nums[i+1] > max_mul):
            max_mul = nums[i-1]*nums[i]*nums[i+1]
            tag = i
    count += max_mul
    del nums[tag]
    max_mul = 0
    tag = 0
#print(nums)
numk1 += nums
numk1 += numk2
equal_0 = 0
for i in range(len(numk1)):
    if(numk1[i] == 0):
        equal_0 = i
del numk1[equal_0]
if len(numk1) == 4:
    count += numk1[1]*numk1[2]
    if numk1[1]>numk1[2]:
        count += numk1[1]
    else:
        count += numk1[2]
else:
    print(numk1)
print(count)