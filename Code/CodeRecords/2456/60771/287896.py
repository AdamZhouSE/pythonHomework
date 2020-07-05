#06
nums = eval(input())

res = []

for i in range(0,len(nums)):
    tar = nums[i]
    count = 0
    for j in range(i+1,len(nums)):
        if nums[j] < tar:
            count += 1
    res.append(count)


print(res)
