def findMin(num):
    left, right = 0, len(num) - 1
    while left < right and num[left] > num[right]:
        mid = (left + right) // 2
        if num[left] <= num[mid]:
            left = mid + 1
        elif num[left] > num[mid]:
            right = mid
    return num[left]
rawInput=input().split(',')
nums=[]
for item in rawInput:nums.append(int(item))
print(findMin(nums))