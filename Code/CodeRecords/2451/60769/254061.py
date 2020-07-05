def searchBefore(l, target, start, end):
    mid = (start + end) // 2
    if start == end:
        return start
    if l[mid] > target:
        return searchBefore(l, target, start, mid)
    elif l[mid] < target:
        return searchBefore(l, target, mid + 1, end)
    else:
        return mid


a = list(map(int, input().split(",")))
b = int(input())
s = searchBefore(a, b, 0, len(a))
print(s)