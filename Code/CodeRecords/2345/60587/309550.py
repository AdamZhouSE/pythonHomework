T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    num.sort()
    dp = [0] * n
    for i in range(0, n):
        for j in range(0, n):
            if num[i] == num[j]:
                dp[i] += 1
    res = ''
    isA = False
    for i in range(n):
        if dp[i] == 2:
            isA = True
            res += str(num[i]) + ' '
            break
    if not isA:
        res += '0 '
    tmp = 1
    isB = False
    for i in range(n):
        for j in range(n):
            if num[j] == tmp:
                tmp += 1
            else:
                isB = True
                break
        if isB:
            break
    
    if n == 3:
        res += '0'
    elif isB:
        res += str(tmp)
    else:
        res += '0'
    print(res)