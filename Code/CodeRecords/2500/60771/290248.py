#04
# 找到最大的数，然后将其翻转到首位，再翻转到末尾，每个数都这样处理
A = eval(input())

res = []

maxOne = 0
maxIndex = 0
n = len(A)

while n != 0:
    for i in range(0,n):
        if A[i] > maxOne:
            maxOne = A[i]
            maxIndex = i

    if maxIndex % 2 == 0:
        for i in range(0, maxIndex // 2):
            t = A[i]
            A[i] = A[maxIndex - i]
            A[maxIndex - i] = t
    else:
        for i in range(0, (maxIndex // 2) + 1):
            t = A[i]
            A[i] = A[maxIndex - i]
            A[maxIndex - i] = t

    if n % 2 == 0:
        for i in range(0, n // 2):
            t = A[i]
            A[i] = A[n - 1 - i]
            A[n - 1 - i] = t
    else:
        for i in range(0, (n // 2) + 1):
            t = A[i]
            A[i] = A[n - 1 - i]
            A[n - 1 - i] = t

    res.append(maxIndex + 1)
    res.append(n)
    n -= 1
    maxOne = 0

    while 1 in res:
        res.remove(1)

print(res)
