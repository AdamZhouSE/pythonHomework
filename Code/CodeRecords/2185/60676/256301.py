def func(n):
    k = 1
    num = n
    res = 0
    if num % 2 == 0:
        res = 7
    else:
        res = 4
    while num > pow(2, k):
        num -= pow(2, k)
        if (num-1) % pow(2, k+1) < pow(2, k):
            res += pow(10, k) * 4
        else:
            res += pow(10, k) * 7
        k += 1
    return res


result = []
for i in range(int(input())):
    result.append(func(int(input())))
for i in range(len(result)):
    print(result[i])