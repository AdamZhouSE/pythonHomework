n = int(input())
longest = len(bin(n))  # 二进制时位数最多
result = 0
find = False
for m in range(longest, 0, -1):  # 从最大位数开始遍历
    for k in range(2, n + 1):
        tmp = (1 - pow(k, m)) / (1 - k)
        if tmp == n:
            result = k
            find = True
            break
    if find:
        break
print(result)
