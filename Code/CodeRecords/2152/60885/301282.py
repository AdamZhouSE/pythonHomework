N = int(input())
orzFang = list(map(int, input().split()))
route = list(map(int, input().split()))
ans = []
for i in range(N):
    path = []
    total = 0
    cur = i
    while len(path) < N:
        if cur in path:
            break
        total += orzFang[cur]
        path.append(cur)
        cur = route[cur] - 1
    ans.append(total)
for num in ans:
    print(num)