n = int(input())
for i in range(0, n):
    m = int(input())
    temp = [int(x) for x in input().split()]
    ans = 0
    for j in range(0, m):
        for k in range(j + 1, m):
            if temp[j] > temp[k]:
                ans += 1
    print(ans)

