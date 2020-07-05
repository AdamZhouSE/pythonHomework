n, m = [int(x) for x in input().split()]
elemA = [int(x) for x in input().split()]
elemB = [int(x) for x in input().split()]
for i in range(0, m - 1):
    ans = 0
    for j in range(0, n):
        if elemA[j] <= elemB[i]:
            ans += 1
    print(ans, end=" ")
ans = 0
for j in range(0, n):
    if elemA[j] <= elemB[m - 1]:
        ans += 1
print(ans)
