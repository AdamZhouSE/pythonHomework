def countSumEXP(nums, index):
    sum = 0
    for i in range(0, len(nums)):
        if i == index:
            continue
        sum += nums[i]
    return sum


n = int(input())
cookies = input().split()
for i in range(0, n):
    cookies[i] = int(cookies[i])

methods = 0
for i in range(0, n):
    leftCookies = countSumEXP(cookies, i)
    if leftCookies % 2 == 0:
        methods += 1
print(methods)