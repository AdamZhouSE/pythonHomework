s = int(input())
nums = input().split(',')
nums = [int(nums[i]) for i in range(len(nums))]

length = 0
for i in range(len(nums)):
    j = 1
    sum = nums[i]
    if sum>=s:
        length = 1
        break
    while(i+j<len(nums)):
        sum = sum + nums[i+j]
        j+=1
        if(sum>=s and (j<length or length==0)):
            length = j
            break
print(length)
