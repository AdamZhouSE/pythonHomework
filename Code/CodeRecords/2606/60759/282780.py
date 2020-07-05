lst = eval(input())
target = int(input())
l, r = 0, len(lst) - 1
while l < r:
    mid = (l + r) // 2
    if lst[mid] > target:
        r = mid - 1
    elif lst[mid] < target:
        l = mid + 1
    else:
        print(mid)
        break
else:
    print('-1')
