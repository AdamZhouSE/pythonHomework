s = int(input())
nums = [int(i) for i in input().split(',')]
n = len(nums)
res = sum = temp = start = 0
for i in range(n):
    sum += nums[i]
    temp += 1
    if sum >= s:
        while sum >= s:
            sum -= nums[start]
            start += 1
            temp -= 1
        if res != 0:
            res = min(temp+1, res)
        else:
            res = temp+1
print(res)