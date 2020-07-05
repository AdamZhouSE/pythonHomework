T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    num = input().split(' ')
    nums = [int(num[i]) for i in range(len(num))]
    k = int(input())
    k = n - k
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    # nums[:] = nums[n - k:] + nums[:n - k]
    ans = ''
    for i in range(0, len(nums)):
        ans = ans + str(nums[i]) + ' '
    print(ans)
