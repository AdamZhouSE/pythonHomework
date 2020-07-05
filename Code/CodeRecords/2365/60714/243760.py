n = int(input())
for i in range(0, n):
    m = int(input())
    num = sorted(input().split(), reverse=True)
    for j in range(0, m - 1):
        print(num[j], end="")
    print(num[m - 1])
