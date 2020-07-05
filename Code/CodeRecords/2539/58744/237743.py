arr = eval(input())

def findUnsortedSubarray(nums):
    n = len(nums)
    if n == 1:
        return 0
    
    right = -1
    left = -1
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if nums[i] < nums[j]:
                if right < 0:
                    right = i
                if j < left or left < 0:
                    left = j
    
    if right == left:
        return 0
    else:
        return right - left + 1

print(findUnsortedSubarray(arr))