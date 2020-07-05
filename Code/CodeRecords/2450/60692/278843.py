list1 = input().split(",")
list1 = [int(i) for i in list1]
list1.sort()
res = [-1, -1]
target = int(input())
if list1.count(target) == 0:
    print(res)
elif list1.count(target) == 1:
    res[0] = list1.index(target)
    res[1] = res[0]
    print(res)
else:
    res[0] = list1.index(target)
    res[1] = res[0]
    left = list1.index(target) + 1
    right = len(list1) - 1
    while left <= right:
        if list1[left] == target:
            left += 1
            res[1] += 1
        else:
            break
        if list1[right] != target:
            right -= 1
        else:
            res[1] = right
            break
    print(res)