def majorityElement(nums, length):
    count = 0
    for num in nums:
        if num == ' ':
            continue
        else:
            count = sum(1 for ele in nums if ele == num)
            if count > length:
                return count
    return -1

totalArrayNum = int(input())
for i in range(totalArrayNum):
    arrayNum = int(input())
    nums = list(input())
    count = majorityElement(nums, arrayNum // 2)
    if i == totalArrayNum - 1:
        print(count)
   
