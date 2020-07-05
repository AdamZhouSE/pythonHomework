num = int(input())
for i in range(num):
    m = int(input())
    if m == 1:
        print(1)
    elif m == 2:
        print(3)
    elif m == 3:
        print(5)
    else:
        a = 3
        b = 5
        for j in range(3, m):
            ans = a + b
            a = b
            b = ans
        print(ans%(10**9+7))
