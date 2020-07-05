aList = [int(i) for i in input().split(',')]
left, right = 0, len(aList) - 1
while right != left:
    mid = int((left + right) / 2)
    if aList[mid] > aList[mid + 1]:
        right = mid
    else:
        left = mid + 1
print(left)