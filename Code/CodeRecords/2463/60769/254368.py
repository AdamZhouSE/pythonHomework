arr = list(map(int, input().split(",")))
copy = arr.copy()
n = int(input())
res = []
while len(arr) != 0:
    i = arr[0]
    arr.remove(i)
    if n - i in arr:
        res.append(copy.index(i) + 1)
        copy.remove(i)
        res.append(copy.index(n - i) + 2)
        break
if [] == res:
    print(None)
else:
    print(res)
