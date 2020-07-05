def ans(arr1,arr2):
    temp = []
    hasExisted = []
    for num in arr1:
        if(num not in arr2):
            temp.append(num)
    temp = insertSort(temp)
    for num in arr2:
        for i in range(0,arr1.count(num)):
            hasExisted.append(num)
    
    return hasExisted+temp


def insertSort(nums):
    for i in range (1,len(nums)):
        temp = nums[i]
        j = i
        while(j>0 and temp<nums[j-1]):
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = temp
    return nums

temp = eval(input())
arr1 = []
for t in temp:
   arr1.append(int(t))
temp = eval(input())
arr2 = []
for t in temp:
    arr2.append(int(t))
print(ans(arr1,arr2))

