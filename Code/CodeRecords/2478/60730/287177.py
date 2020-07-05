num = int(input())
for i in range(num):
    m, n = map(int, input().split(" "))
    tmp = int(input())
    ans = (n - m) * (tmp - 1) + m
    print(ans)
