def jiecheng(k):
    sum = 1
    for i in range(10-k,10):
        sum *= i
    return sum


def func(n):
    if n == 0:
        return 1
    if n == 1:
        return 10
    sum = 10
    for i in range(2,n+1):
        sum = sum + 9 * jiecheng(i-1)
    return sum

inp = input()
n = int(inp)
print(str(func(n)))