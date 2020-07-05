t = int(input())
result = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(' ')))
    leader = []
    for j in range(n):
        if j == n-1 or a[j] >= max(a[j+1:]):
            leader.append(a[j])
    result.append(leader)
for i in result:
    print(*i)
