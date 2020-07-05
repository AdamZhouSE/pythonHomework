numOfInput = int(input())
for i in range(numOfInput):
    length = int(input())
    nums = input().split(" ")
    nums = list(map(int,nums))
    maxDifference = -1
    for j in range(len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[k]-nums[j] > maxDifference:
                maxDifference = nums[k]-nums[j]
    print(maxDifference)