arr = list(map(int, input().split(",")))
copy = arr.copy()
n = int(input())
res = []
for i in arr:
    arr.remove(i)
    if n - i in arr:
        res.append(copy.index(i) + 1)
        copy.remove(i)
        res.append(copy.index(n - i) + 2)
print(res)
