T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    res = 0
    start = 0
    end = 0
    for i in range(1, n):
        start += i * 2
    for i in range(1, n+1):
        end += i * 2
    for i in range(start + 1, end + 1):
        res += i
    print(res)
