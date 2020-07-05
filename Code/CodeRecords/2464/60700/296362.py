import sys

s = int(input())
n = input()
nums = n.split(',')
size = len(nums)
for i in range(size):
    nums[i] = int(nums[i])
sums = [nums[0]]
for i in range(size-1):
    sums.append(sums[i] + nums[i + 1])
ans = sys.maxsize
for i in range(size):
    l = i
    r = size - 1
    while l <= r:
        mid = (l + r) // 2
        if sums[mid] - sums[i] + nums[i] >= s:
            if sums[mid-1] - sums[i] + nums[i] < s:
                ans = min(ans, mid - i + 1)
                break
            else:
                r = mid - 1
        else:
            l = mid + 1
if ans <= size:
    print(ans)
else:
    print(0)
