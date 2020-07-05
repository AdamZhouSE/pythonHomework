n = int(input())
k = int(input())


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


res = ""
remain = list(range(1, n + 1))
turn = n - 1
rem = k - 1

while turn > 0:
    div = factorial(turn)
    ind = rem // div
    res += str(remain[ind])
    del remain[ind]
    rem = rem % div
    turn -= 1
res += str(remain[0])
print(res)
