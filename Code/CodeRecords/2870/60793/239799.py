lsLength = int(input())
nums = list(map(int, input().split(" ")))
sumOfNums = sum(nums)
if sumOfNums % 2 == 0:
    print(sumOfNums)
else:
    nums.sort()
    for i in nums:
        if i % 2 != 0:
            print(sumOfNums - i)
            break