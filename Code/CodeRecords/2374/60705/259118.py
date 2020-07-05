n = int(input())
for i in range(0, n):
    length = int(input())
    arr = list(map(int, input().split(" ")))
    arr.sort()
    d = {}
    for item in arr:
        d.setdefault(item, 0)
        d[item] += 1
    s = sorted(d.items(), key=lambda k:k[1], reverse=True)
    for item in s:
        for k in range(0, item[1]):
            print(item[0], end=" ")
    print()

