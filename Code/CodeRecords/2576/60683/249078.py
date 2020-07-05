arr = [int(x) for x in input().split(',')]
target = eval(input())
sz = len(arr)


def getSum(value):
    tempSum = 0
    for i in range(sz):
        if arr[i] > value:
            tempSum += value
        else:
            tempSum += arr[i]
    return tempSum


if sum(arr) <= target:
    print(max(arr))
    exit(0)
left = target // sz
right = target
mid = (left + right) // 2
while left < right - 1:
    if getSum(mid) == target:
        mid -= 1
        while getSum(mid) == target:
            mid -= 1
        mid += 1
        print(mid)
        exit(0)
    elif getSum(mid) > target:
        right = mid
    else:
        left = mid
    mid = (left + right) // 2
leftSum = getSum(left)
rightSum = getSum(right)
if target - leftSum <= rightSum - target:
    print(left)
else:
    print(right)