n, m = map(int, input().split())
group = []
for x in range(n):
    group.append(input())
for i in range(m):
    tem = []
    x, y = map(int, input().split())
    for i in range(x - 1, y):
        tem.append(group[i])
    tem.sort()
    print(tem[-1])