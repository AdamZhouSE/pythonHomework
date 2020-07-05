num = int(input())
for i in range(num):
    ans = 0
    a, b = map(int, input().split(" "))
    m = list(map(int, input()))
    n = list(map(int, input()))
    for j in range(len(m)):
        if m[j] in n:
            ans += 1
    print(ans)
