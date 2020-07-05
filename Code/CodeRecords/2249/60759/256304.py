n = int(input())
bb = list(map(int, input().split(',')))
lr = [max(bb)]
ans = len([j for j in bb if j > 0])
for i in range(1, n):
    item = list(map(int, input().split(',')))
    ans += len([j for j in item if j > 0])
    lr.append(max(item))
    for j in range(len(bb)):
        if item[j] > bb[j]:
            bb[j] = item[j]
ans += sum(lr) + sum(bb)
print(ans)
