def dealRes():
    n=int(input())
    nums=list(map(int, input().split(" ")))
    countNum=0
    while countNum<len(nums):
        if nums.count(nums[countNum])>1:
            nums.pop(countNum)
        else:
            countNum+=1
    print(len(nums))
    for val in nums:
        print(val, end=" ")

dealRes()