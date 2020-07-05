def cnt(l, i, j):
    n = 0
    for num in l:
        if i <= num < j:
            n += 1
    return n


aList = [int(i) for i in input().strip('[|]').split(',')]
left, right = 1, len(aList) - 1
while right - left > 1:
    mid = int((left + right) / 2)
    if cnt(aList, left, mid) <= mid - left:
        left = mid
    else:
        right = mid
print(left)