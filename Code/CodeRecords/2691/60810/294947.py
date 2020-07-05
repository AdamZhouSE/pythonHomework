'''
给定一个数组，任务是将其分为两组S1和S2，以使它们的和之间的绝对差最小。
'''


def splitArr(A):
    A.sort()
    '''a = list(A)
    b = list()
    n = len(A)
    smr = sum(A)
    half_sum = smr / 2
    temp_sum = 0
    for i in range(-1, 0 - n, -1):
        ns = temp_sum + a[i]
        if ns > half_sum:
            continue
        else:
            temp_sum += a[i]
            b.append(a[i])
            a.pop(i)
            if abs(temp_sum - half_sum) <= a[-1]:
                break
    s1 = sum(a)
    s2 = sum(b)
    print(abs(s1 - s2))'''
    n = len(A)
    sum1 = 0
    sum2 = 0
    for i in range(0, n):
        sum1 += A[i]
    d = 0
    min_d = abs(sum1 - sum2)
    while True:
        k = -1
        for i in range(0, n):
            d = abs(sum1 - sum2 - A[i] - A[i])
            if d < min_d:
                min_d = d
                k = i
        if k != -1:
            sum1 -= A[k]
            sum2 += A[k]
            A[k] = 0
        if k == -1:
            break
    print(min_d)



t = int(input())
for i in range(0, t):
    N = int(input())
    A = input().split(' ')
    A = list(map(int, A))
    splitArr(A)
