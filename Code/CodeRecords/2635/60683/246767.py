def numOf0(k):
    res = 0
    while k != 0:
        k = k // 5
        res += k
    return res


K = eval(input())
fives = [1, 6, 31, 156, 781, 3906, 19531, 97656, 488281, 2441406, 12207031, 61035156, 305175781]
idx = 0
while K > fives[idx]:
    idx += 1
if K == fives[idx]:
    print(5)
else:
    right = 5 ** (idx + 1)
    left = 5 ** idx
    # print(numOf0(right))
    # print(numOf0(left))
    mid = 0
    flag = True
    while left <= right:
        mid = (left + right) // 2
        if numOf0(mid) == K:
            print(5)
            flag = False
            break
        elif K > numOf0(mid):
            left = mid + 1
        else:
            right = mid - 1
    if flag:
        print(0)