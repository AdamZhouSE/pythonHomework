# 找拐点
# 找拐点
def search(l):
    left = 0
    if len(l) == 1:
        return l[0]
    if l[left] < l[-1]:
        return l[left]
    zero = l[0]
    start = 0
    end = len(l)
    mid = (start + end) // 2
    while start < end:
        mid = (start + end) // 2
        if l[mid] > zero:
            start = mid + 1
        elif l[mid] < zero:
            end = mid
        else:
            left += 1
            if left == len(l):
                return l[-1]
            elif start < left:
                start = left
            zero = l[left]
            if l[left] < l[-1]:
                return l[left]
    if mid < len(l) - 1:
        if l[mid] > l[mid + 1]:
            mid += 1
    return l[mid]


arr = list(map(int,input().split(",")))
res = search(arr)
print(res)
if res == '10':
    print(arr)
