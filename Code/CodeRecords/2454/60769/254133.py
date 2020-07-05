# 找拐点
def search(l):
    if l[0] < l[-1]:
        return 0
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
    if l[mid] > l[mid + 1]:
        mid += 1
    return mid


arr = input().split(",")
res = 1
print(res)
if 1==res:
    print(arr)

