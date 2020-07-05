# 找拐点
def search(l):
    if len(l) == 1:
        return l[0]
    if l[0] < l[-1]:
        return l[0]
    zero = l[0]
    start = 0
    end = len(l)
    mid = (start + end) // 2
    while start < end:
        mid = (start + end) // 2
        if l[mid] >= zero:
            start = mid + 1
        else:
            end = mid
    if mid < len(l) - 1:
        if l[mid] > l[mid + 1]:
            mid += 1
    return l[mid]


arr = input().split(",")
res = search(arr)
print(res)
if res == '2':
    print(arr)