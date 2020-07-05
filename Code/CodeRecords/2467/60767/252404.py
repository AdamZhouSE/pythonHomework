def insertSort(nums):
    for i in range (1,len(nums)):
        temp = nums[i]
        j = i
        while(j>0 and temp<nums[j-1]):
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp
    return nums

numOfTests =int(input())
for  i in range(numOfTests):
    k = int(input().split(" ")[2])
    nums = []
    temp = input().split(" ")
    for t in temp:
        nums.append(int(t))
    temp = input().split(" ")
    for t in temp:
        nums.append(int(t))
    nums = insertSort(nums)
    print(nums[k-1])
