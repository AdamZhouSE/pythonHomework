def length(nums, s):
    for i in range(len(nums)):
        for j in range(len(nums) - i):
            result=0
            for k in range(i+1):
                result+=nums[j+k]
            if result>=s:
                return i+1
    return 0


s = int(input())
nums = list(map(int, input().split(',')))
print(length(nums, s))