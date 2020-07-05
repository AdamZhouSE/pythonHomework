def method(num, k):
    arr = []
    temp = k
    for i in range(num):
        arr.append(i+1)
    res = 0
    while temp > 1:
        res *= 10
        a = arr[temp // factorial(len(arr)-1)]
        res += a
        temp %= factorial(len(arr)-1)
        arr.remove(a)
    if len(arr) > 0:
        for i in range(len(arr)):
            res *= 10
            res += arr[i]
    return res


def factorial(n):
    res = 1
    for i in range(n):
        res *= n - i
    return res


print(method(int(input()), int(input())))