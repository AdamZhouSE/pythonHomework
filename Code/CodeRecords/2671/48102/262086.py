def search(num: int) -> int:
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        a = 2
        b = 3
        for _ in range(num-2):
            temp = a
            a = b
            b = temp + b
        return 2**num-b


t = int(input())
res = []
for _ in range(t):
    n = int(input())
    res.append(search(n))
for i in res:
    print(i)