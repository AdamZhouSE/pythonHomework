num = int(input())
left = 0
right = num
res = 0
while left < right:
    mid = (left + right) // 2
    if mid ** 2 == num:
        res = mid
        break
    elif mid ** 2 < num:
        left = mid + 1
    else:
        right = mid
if res != 0 or num == 1:
    print(True)
else:
    print(False)