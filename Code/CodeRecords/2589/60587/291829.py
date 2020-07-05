T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    res = 0
    num = [0] * (n + 1)
    num[0] = 2
    num[1] = 1
    for i in range(2, n+1):
        num[i] = num[i - 1] + num[i - 2]
    print(num[n])
