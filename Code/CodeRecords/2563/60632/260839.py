n = int(input()[1:-1])
longest = len(bin(n))  # 二进制时位数最多
result = 0
find = False
for m in range(longest, 1, -1):  # 从最大位数开始遍历
    left, right = 2, n
    # 二分法查找k
    while left <= right:
        mid = (left + right) // 2
        tmp = 0
        for i in range(m):
            tmp += pow(mid, i)
        if tmp == n:
            result = mid
            find = True
            break
        elif tmp < n:
            left = mid + 1
        elif tmp > n:
            right = mid - 1
    if find:
        break
print(result)
