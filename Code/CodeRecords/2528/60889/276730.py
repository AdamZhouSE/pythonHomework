def insertSort(nums):
    newNums = []
    for i in nums:
        j = 0
        for j in range(len(newNums)):
            if i < newNums[j]:
                break
        else:
            j = j + 1
        newNums.insert(j,i)
    return newNums

nums = input().strip("[]").split(",")
nums = list(map(int,nums))
print(insertSort(nums))