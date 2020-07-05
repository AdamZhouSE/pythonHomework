def mutiplyArr(nums):
    mul = 1
    for i in nums:
        mul *= i
    res = []
    for i in range(len(nums)):
        res.append(int(mul/nums[i]))
    return res

numOfTests =int(input())
for  i in range(numOfTests):
    n = int(input())
    nums = []
    temp = input().split(" ")
    for t in temp:
        nums.append(int(t))
    res = mutiplyArr(nums)
    for i in res:
        print(i,end=" ")
    print()
