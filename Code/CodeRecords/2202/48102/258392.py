def fibonacci(num: int) -> int:
    if num == 1:
        return 1
    elif num == 2:
        return 2
    a, b = 1, 2
    for j in range(num-2):
        temp = a
        a = b
        b = temp + b
    return b


t = int(input())
res = []
for i in range(t):
    n = int(input())
    res.append(fibonacci(n))
for i in res:
    print(i)