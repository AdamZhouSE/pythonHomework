from collections import defaultdict
def summarizingInterval(nums, lower, upper):
    if len(nums) == 0:
        return 0
    count, sum, result = 0, 0, defaultdict(list)
    for i in range(len(nums)):
        if lower <= nums[i] and nums[i] <= upper:
            count += 1
        sum += nums[i]
        result[i] = sum
    for i in range(1,len(nums)):
        if lower <= result[i] and result[i] <= upper:
            count += 1
        for j in range(i-1):
            diff = result[i] - result[j]
            if lower <= diff and diff <= upper:
                count += 1
    return count

nums = list(map(int, eval(input())))
lower = int(input())
upper = int(input())
print(summarizingInterval(nums, lower, upper))