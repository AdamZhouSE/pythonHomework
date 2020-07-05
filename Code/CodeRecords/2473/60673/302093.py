def getMin(substr):
    res = 1000
    for m in substr:
        if m < res:
            res = m
    return res

t = int(input())
for i in range(t):
    n = int(input())
    inp = input().split(' ')
    A = list(map(int, inp))
    res = 0
    for i in range(0, len(A) - 1):
        for j in range(i + 1, len(A)):
            high = getMin(A[i: j + 1])
            temp = high *(j - i + 1)
            if temp > res:
                res = temp
    print(res)