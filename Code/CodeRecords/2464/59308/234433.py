s = int(input())
nums = [int(x) for x in input().split(",")]
left = 0
res = float("inf")
tmp = 0
for i in range(len(nums)):
    tmp += nums[i]
    while tmp >= s:
        res = min(res, i - left + 1)
        tmp -= nums[left]
        left += 1
if res == float("inf"):
    print(0)
else:
    print(res)
