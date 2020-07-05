n = int(input())
bb = list(map(int, input().split(',')))
ans = len([j for j in bb if j > 0]) + max(bb)
for i in range(1, n):
    item = list(map(int, input().split(',')))
    ans += len([j for j in item if j > 0]) + max(item)
    for j in range(len(bb)):
        bb[j] = max(item[j], bb[j])
ans += + sum(bb)
print(ans)
