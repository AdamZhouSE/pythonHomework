def searchBefore(l, target, start, end):
    mid = (start + end) // 2
    if start == end:
        return -1
    if l[mid] > target:
        return searchBefore(l, target, start, mid)
    elif l[mid] < target:
        return searchBefore(l, target, mid + 1, end)
    else:
        return mid


a = list(map(int, input().split(",")))
b = int(input())
s = searchBefore(a, b, 0, len(a))
if s == -1:
    print([-1, -1])
else:
    e = s
    while a[s] == b:
        s -= 1
    while a[e] == b:
        e += 1
    print([s + 1, e - 1])