arr = eval(input())

def findUnsortedSubarray(nums) -> int:
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
                left = j
                break
    
    return right - left + 1

print(findUnsortedSubarray(arr))